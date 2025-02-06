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


def import_players(api_url, csv_endpoint: Tuple[str, str], auth_token, refresh_token, username, password):
    """
    Import players from a CSV file and upload photos as files, avoiding duplicates.
    Refresh the token after every 50 requests.
    """
    headers = {'Authorization': f"Bearer {auth_token}"}
    PHOTOS_PATH = 'D:/backups/player_photos/'
    request_count = 0  # Track the number of requests made
    csv_path = os.path.join('./mysql_csv', csv_endpoint[0])

    file = open(csv_path, mode='r', encoding='utf-8')
    reader = csv.DictReader(file)
    rows = list(reader)

    for row in rows:
        print(f"Adding player with {row['id']}: {row['first_name']} {row['last_name']}")
        # Refresh the token every 50 requests
        if request_count % 50 == 0 and request_count > 0:
            print("Refreshing token...")
            auth_token = refresh_auth_token(api_url, refresh_token)
            if not auth_token:
                print("Failed to refresh token. Stopping operation.")
                return
            headers['Authorization'] = f"Bearer {auth_token}"
            print("Token refreshed")

        # Check if the resource already exists
        player_id = row.get('id')  # Use the ID field as a unique identifier
        if player_id:
            check_response = requests.get(f"{api_url}/{csv_endpoint[1]}/{player_id}/", headers=headers)
            if check_response.status_code == 200:
                print(f"Resource with ID {player_id} already exists in {csv_endpoint[1]}, skipping...")
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
                f"{api_url}/{csv_endpoint[1]}",
                data={
                    'id': row['id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'date_of_birth': row['date_of_birth'],
                    'nationality': row['nationality'],
                    'alias': row['alias'],
                    'gender': row['gender'],
                },
                headers=headers,
                files=files if files else None
            )

            if files:
                files['photo'].close()

            # print("Response: ", response)

            if response.status_code == 201:
                print(f"Data inserted into {csv_endpoint[1]}: {row}")
            elif response.status_code == 500:
                print(f"Error inserting data into {csv_endpoint[1]}: {response.status_code}")
                return
            elif response.status_code == 401:
                print(f"Unauthorized: Token might have expired.")
                return
            else:
                print(f"Error inserting data into {csv_endpoint[1]}: {response.status_code}")

            request_count += 1  # Increment request count

        except Exception as e:
            print(f"Exception occurred while uploading data: {e}")

    print(f"Processed {len(rows)} entries from file: {csv_endpoint[0]}")

def import_matches(api_url, csv_endpoint: Tuple[str, str], auth_token, refresh_token, username, password):
    """
    Since the old matches all were of 1 single game, we can just import them as the game data.
    """
    headers = {'Authorization': f"Bearer {auth_token}"}
    request_count = 0  # Track the number of requests made
    csv_path = os.path.join('./mysql_csv', csv_endpoint[0])

    file = open(csv_path, mode='r', encoding='utf-8')
    reader = csv.DictReader(file)
    rows = list(reader)

    for row in rows:
        print(f"Adding match with {row['id']}")
        # Refresh the token every 50 requests
        if request_count % 50 == 0 and request_count > 0:
            print("Refreshing token...")
            auth_token = refresh_auth_token(api_url, refresh_token)
            if not auth_token:
                print("Failed to refresh token. Stopping operation.")
                return
            headers['Authorization'] = f"Bearer {auth_token}"
            print("Token refreshed")

        # Check if the resource already exists
        # match_id = row.get('id')  # Use the ID field as a unique identifier
        # if match_id:
        #     check_response = requests.get(f"{api_url}/{csv_endpoint[1]}/{match_id}/", headers=headers)
        #     if check_response.status_code == 200:
        #         print(f"Resource with ID {match_id} already exists in {csv_endpoint[1]}, skipping...")
        #         continue

        # Post the data if it does not already exist
        try:
            # Create match first and then add the game
            if csv_endpoint[1] == 'matches/singles':
                response_match = requests.post(
                    f"{api_url}/{csv_endpoint[1]}/",
                    data={
                        'date': row['date'],
                        'player1': row['player1_id'],
                        'player2': row['player2_id'],
                    },
                    headers=headers
                )

                if response_match.status_code != 201:
                    print(f"Error adding match: {response_match.status_code}")
                    Exception("Error adding match")

                print(f"Match added successfully: {response_match.json()}")

                response_game = requests.post(
                    f"{api_url}/matches/singles-games/",
                    data={
                        'match': response_match.json()['id'],
                        'player1_score': row['player1_score'],
                        'player2_score': row['player2_score'],
                    },
                    headers=headers
                )

                if response_game.status_code == 201:
                    print(f"Game added successfully to match {response_match.json()['id']}")

            elif csv_endpoint[1] == 'matches/doubles':
                response_match = requests.post(
                    f"{api_url}/{csv_endpoint[1]}/",
                    data={
                        'date': row['date'],
                        'team1_player1': row['team1_player1_id'],
                        'team1_player2': row['team1_player2_id'],
                        'team2_player1': row['team2_player1_id'],
                        'team2_player2': row['team2_player2_id'],
                    },
                    headers=headers
                )

                if response_match.status_code != 201:
                    print(f"Error adding match: {response_match.status_code}")
                    Exception("Error adding match")

                response_game = requests.post(
                    f"{api_url}/matches/doubles-games/",
                    data={
                        'match': response_match.json()['id'],
                        'team1_score': row['team1_score'],
                        'team2_score': row['team2_score'],
                    },
                    headers=headers
                )
        except Exception as e:
            print(f"Exception occurred while uploading data: {e}")

def main():
    # Define your backend API URL
    API_URL = 'http://localhost:8000/api'  # Replace with your actual API URL
    USERNAME = 'admin'  # Replace with your username
    PASSWORD = 'admin'  # Replace with your password

    # Define the list of CSV files and their corresponding endpoints
    CSV_ENDPOINT = [
        ('players_player.csv', 'players/player/'),
        ('matches_singlesmatch.csv', 'matches/singles'),
        ('matches_doublesmatch.csv', 'matches/doubles'),
    ]

    # Obtain initial authentication token and refresh token
    AUTH_TOKEN, REFRESH_TOKEN = get_auth_token(API_URL, USERNAME, PASSWORD)
    if not AUTH_TOKEN or not REFRESH_TOKEN:
        print("Error: Unable to obtain initial authentication tokens.")
        return

    print("Token obtained")

    response_lookup_season = requests.get(f"{API_URL}/seasons/1", headers={'Authorization': f"Bearer {AUTH_TOKEN}"})

    if response_lookup_season.status_code != 200:
        response = requests.post(f"{API_URL}/seasons/", json={
            'name': 'Default Season',
            'description': 'Default season for testing purposes',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'singles_points_for_win': 2,
            'singles_points_for_loss': 0,
            'doubles_points_for_win': 2,
            'doubles_points_for_loss': 0
        },
            headers={'Authorization': f"Bearer {AUTH_TOKEN}"})

        if not response.status_code == 201:
            print(f"Error creating default season: {response.status_code}")
            return

    # Call the import function
    # import_csv_to_api(API_URL, CSV_ENDPOINT, auth_token=AUTH_TOKEN, refresh_token=REFRESH_TOKEN, username=USERNAME, password=PASSWORD)

    print("Loading players")
    import_players(API_URL, CSV_ENDPOINT[0], AUTH_TOKEN, REFRESH_TOKEN, USERNAME, PASSWORD)
    import_matches(API_URL, CSV_ENDPOINT[1], AUTH_TOKEN, REFRESH_TOKEN, USERNAME, PASSWORD)
    import_matches(API_URL, CSV_ENDPOINT[2], AUTH_TOKEN, REFRESH_TOKEN, USERNAME, PASSWORD)

    print("Everything finished")


if __name__ == '__main__':
    main()
