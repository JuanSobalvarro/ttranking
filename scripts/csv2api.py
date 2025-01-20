import os
import csv
import requests
from typing import Tuple


def get_auth_token(api_url: str, username: str, password: str) -> Tuple[str, str]:
    """
    Retrieve a new authentication token and refresh token.
    """
    try:
        response = requests.post(f"{api_url}/token/", json={'username': username, 'password': password})
        response.raise_for_status()
        tokens = response.json()
        return tokens.get('access'), tokens.get('refresh')
    except Exception as e:
        print(f"Error obtaining authentication token: {e}")
        return None, None


def refresh_auth_token(api_url: str, refresh_token: str) -> str:
    """
    Refresh the authentication token using the refresh token.
    """
    try:
        response = requests.post(f"{api_url}/token-refresh/", json={'refresh': refresh_token})
        response.raise_for_status()
        return response.json().get('access')
    except Exception as e:
        print(f"Error refreshing authentication token: {e}")
        return None


def import_csv_to_api(api_url, csv_endpoint, auth_token, refresh_token, username, password):
    """
    Import data from a CSV file and upload photos as files, avoiding duplicates.
    Refresh the token after every 50 requests.
    """
    headers = {'Authorization': f"Bearer {auth_token}"}
    PHOTOS_PATH = 'D:/backups/player_photos/'
    request_count = 0  # Track the number of requests made

    for csv_file, endpoint in csv_endpoint:
        csv_path = os.path.join('./mysql_csv', csv_file)

        if not os.path.exists(csv_path):
            print(f"Error: The file '{csv_path}' does not exist.")
            continue

        print(f"Processing file: {csv_file} for endpoint: {endpoint}")

        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            for row in rows:
                # Refresh the token every 50 requests
                if request_count % 50 == 0 and request_count > 0:
                    print("Refreshing token...")
                    auth_token = refresh_auth_token(api_url, refresh_token)
                    if not auth_token:
                        print("Failed to refresh token. Stopping operation.")
                        return
                    headers['Authorization'] = f"Bearer {auth_token}"
                    print("Token refreshed")

                # Map foreign keys
                for key in list(row.keys()):
                    if key.endswith('_id'):
                        row[key[:-3]] = row.pop(key)

                # Check if the resource already exists
                resource_id = row.get('id')  # Use the ID field as a unique identifier
                if resource_id:
                    check_response = requests.get(f"{api_url}/{endpoint}/{resource_id}/", headers=headers)
                    if check_response.status_code == 200:
                        print(f"Resource with ID {resource_id} already exists in {endpoint}, skipping...")
                        continue

                # Prepare the multipart form data
                files = {}
                if row.get('photo'):
                    photo_path = os.path.join(PHOTOS_PATH, f"{row.get('id')}.png")
                    if os.path.exists(photo_path):
                        files['photo'] = open(photo_path, 'rb')
                    else:
                        print(f"Photo not found for player ID {row['id']}, skipping photo upload.")
                        row.pop('photo', None)

                # Post the data if it does not already exist
                try:
                    response = requests.post(
                        f"{api_url}/{endpoint}/",
                        data=row,
                        headers=headers,
                        files=files if files else None
                    )

                    if files:
                        files['photo'].close()

                    if response.status_code == 201:
                        print(f"Data inserted into {endpoint}: {row}")
                    elif response.status_code == 500:
                        print(f"Error inserting data into {endpoint}: {response.status_code} - {response.text}")
                        return
                    elif response.status_code == 401:
                        print(f"Unauthorized: Token might have expired.")
                        return
                    else:
                        print(f"Error inserting data into {endpoint}: {response.status_code}")

                    request_count += 1  # Increment request count

                except Exception as e:
                    print(f"Exception occurred while uploading data: {e}")

            print(f"Processed {len(rows)} entries from file: {csv_file}")


def main():
    # Define your backend API URL
    API_URL = 'http://localhost:8000/api'  # Replace with your actual API URL
    USERNAME = 'admin'  # Replace with your username
    PASSWORD = 'admin'  # Replace with your password

    # Define the list of CSV files and their corresponding endpoints
    CSV_ENDPOINT = [
        ('players_player.csv', 'players'),
        ('matches_singlesmatch.csv', 'matches/singles'),
        ('matches_doublesmatch.csv', 'matches/doubles'),
    ]

    # Obtain initial authentication token and refresh token
    AUTH_TOKEN, REFRESH_TOKEN = get_auth_token(API_URL, USERNAME, PASSWORD)
    if not AUTH_TOKEN or not REFRESH_TOKEN:
        print("Error: Unable to obtain initial authentication tokens.")
        return

    print("Token obtained")

    # Create default season
    response = requests.post(f"{API_URL}/seasons/", json={
        'name': 'Default Season',
        'start_date': '2021-01-01',
        'end_date': '2021-12-31'}, headers={'Authorization': f"Bearer {AUTH_TOKEN}"})

    if not response.status_code == 201:
        print(f"Error creating default season: {response.status_code} - {response.text}")
        return

    # Call the import function
    import_csv_to_api(API_URL, CSV_ENDPOINT, auth_token=AUTH_TOKEN, refresh_token=REFRESH_TOKEN, username=USERNAME, password=PASSWORD)

    print("Everything finished")


if __name__ == '__main__':
    main()
