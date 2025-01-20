import os
import csv


def get_file_scp(filepath, keypath, user, host, destination):
    """
    Download a file from a remote server using SCP.
    :param filepath:
    :param keypath:
    :param user:
    :param host:
    :param destination:
    :return:
    """

    os.system(f'scp -i {keypath} {user}@{host}:{filepath} {destination}')

def get_photo_from_csv(filepath):
    """
    Read a CSV file and returns a dict of data with the id as key and the photo as value.
    :param filepath:
    :return:
    """
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        data: dict[str, str] = {}

        for row in reader:
            data[row['id']] = row['photo']

        return data

    return None

def main():
    user = 'ubuntu'
    host = '3.208.17.51'
    keypath = 'D:/sshkeys/ttranking.pem'
    destination = 'D:\\backups\\player_photos\\'
    file_path = '/home/ubuntu/tt-ranking-system/ttranking/media/'
    csv_path = './mysql_csv/players_player.csv'

    data = get_photo_from_csv(csv_path)
    print(data)

    for player_id, photo in data.items():
        if not photo:
            continue

        print(f"Getting photo for player ID: {player_id}")

        get_file_scp(f'{file_path}{photo}', keypath, user, host, destination)

        # Rename the file
        original_path = os.path.join(destination, photo.split('/')[-1])
        new_path = os.path.join(destination, f"{player_id}.png")
        os.rename(original_path, new_path)
        print(f"Renamed {original_path} to {new_path}")


if __name__ == "__main__":
    main()
