import os
import csv
import argparse
import requests
from typing import Tuple

# Define the list of CSV files and their corresponding endpoints
CSV_ENDPOINT = [
    ('players_player.csv', 'players/player/'),
    ('matches_singlesmatch.csv', 'matches/singles'),
    ('matches_doublesmatch.csv', 'matches/doubles'),
]


def get_auth_token(api_url: str, username: str, password: str) -> Tuple[str, str]:
    """Retrieve a new authentication token and refresh token."""
    try:
        response = requests.post(f"{api_url}/token/", json={'username': username, 'password': password})
        response.raise_for_status()
        tokens = response.json()
        return tokens.get('access'), tokens.get('refresh')
    except Exception as e:
        print(f"Error obtaining authentication token: {e}")
        return None, None


def refresh_auth_token(api_url: str, refresh_token: str) -> str:
    """Refresh the authentication token using the refresh token."""
    try:
        response = requests.post(f"{api_url}/token-refresh/", json={'refresh': refresh_token})
        response.raise_for_status()
        return response.json().get('access')
    except Exception as e:
        print(f"Error refreshing authentication token: {e}")
        return None


def import_players(api_url, csv_endpoint: Tuple[str, str], auth_token, refresh_token, username, password):
    """Import players from a CSV file and upload photos as files, avoiding duplicates."""
    headers = {'Authorization': f"Bearer {auth_token}"}
    PHOTOS_PATH = 'D:/backups/player_photos/'
    request_count = 0  # Track the number of requests made
    csv_path = os.path.join('./mysql_csv', csv_endpoint[0])

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        print(f"Adding player with {row['id']}: {row['first_name']} {row['last_name']}")

        # Refresh token every 50 requests
        if request_count % 10 == 0 and request_count > 0:
            print("Refreshing token...")
            auth_token = refresh_auth_token(api_url, refresh_token)
            if not auth_token:
                print("Failed to refresh token. Stopping operation.")
                return
            headers['Authorization'] = f"Bearer {auth_token}"
            print("Token refreshed")

        # Check if the resource already exists
        player_id = row.get('id')
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

        # Post data if it does not exist
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

            if response.status_code == 201:
                print(f"Data inserted into {csv_endpoint[1]}: {row}")
            elif response.status_code in [500, 401]:
                print(f"Error inserting data: {response.status_code}. Stopping process.")
                return
            else:
                print(f"Error inserting data into {csv_endpoint[1]}: {response.status_code}")

            request_count += 1  # Increment request count

        except Exception as e:
            print(f"Exception occurred while uploading data: {e}")

    print(f"Processed {len(rows)} entries from file: {csv_endpoint[0]}")


def import_matches(api_url, csv_endpoint: Tuple[str, str], auth_token, refresh_token, username, password):
    """Import matches from a CSV file."""
    headers = {'Authorization': f"Bearer {auth_token}"}
    request_count = 0  # Track the number of requests made
    csv_path = os.path.join('./mysql_csv', csv_endpoint[0])

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        print(f"Adding match with {row['id']}")

        # Refresh token every 50 requests
        if request_count % 10 == 0 and request_count > 0:
            print("Refreshing token...")
            auth_token = refresh_auth_token(api_url, refresh_token)
            if not auth_token:
                print("Failed to refresh token. Stopping operation.")
                return
            headers['Authorization'] = f"Bearer {auth_token}"
            print("Token refreshed")

        try:
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

                if response_match.status_code == 201:
                    print(f"Match added: {response_match.json()}")
                else:
                    raise Exception(f"Error adding match: {response_match.status_code}")

                requests.post(
                    f"{api_url}/matches/singles-games/",
                    data={
                        'match': response_match.json()['id'],
                        'player1_score': row['player1_score'],
                        'player2_score': row['player2_score'],
                    },
                    headers=headers
                )

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

                if response_match.status_code == 201:
                    print(f"Match added: {response_match.json()}")
                else:
                    raise Exception(f"Error adding match: {response_match.status_code}")

                requests.post(
                    f"{api_url}/matches/doubles-games/",
                    data={
                        'match': response_match.json()['id'],
                        'team1_score': row['team1_score'],
                        'team2_score': row['team2_score'],
                    },
                    headers=headers
                )

        except Exception as e:
            print(f"Exception occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Import data into the TT Ranking System API.")
    parser.add_argument("--api_url", required=True, help="API URL (e.g., https://ttranking.example.com/api)")
    parser.add_argument("--username", required=True, help="Username for authentication")
    parser.add_argument("--password", required=True, help="Password for authentication")

    args = parser.parse_args()
    api_url = args.api_url
    username = args.username
    password = args.password

    auth_token, refresh_token = get_auth_token(api_url, username, password)
    if not auth_token or not refresh_token:
        print("Error: Unable to obtain authentication tokens.")
        return

    print("Token obtained")

    print("Loading players")
    import_players(api_url, CSV_ENDPOINT[0], auth_token, refresh_token, username, password)
    import_matches(api_url, CSV_ENDPOINT[1], auth_token, refresh_token, username, password)
    import_matches(api_url, CSV_ENDPOINT[2], auth_token, refresh_token, username, password)

    print("Everything finished")


if __name__ == '__main__':
    main()
