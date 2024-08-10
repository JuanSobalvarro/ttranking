import os

# Backup configuration
BACKUP_DIR = '~/backups/'  # Replace with your backup directory
DB_NAME = 'ttranking'   # Replace with your database name


def check_backup():
    # Get the latest backup file
    try:
        files = [f for f in os.listdir(BACKUP_DIR) if f.endswith('.sql')]
        if not files:
            raise FileNotFoundError("No backup files found.")

        latest_backup_file = max(files, key=lambda f: os.path.getmtime(os.path.join(BACKUP_DIR, f)))
        backup_file_path = os.path.join(BACKUP_DIR, latest_backup_file)

        # Check if the backup file exists
        if not os.path.exists(backup_file_path):
            raise FileNotFoundError(f"Backup file {backup_file_path} does not exist.")

        # Check if the backup file is not empty
        if os.path.getsize(backup_file_path) == 0:
            raise ValueError(f"Backup file {backup_file_path} is empty.")

        # Optional: Check if the backup file contains the expected content
        with open(backup_file_path, 'r') as f:
            content = f.read()
            if DB_NAME not in content:
                raise ValueError(f"Backup file {backup_file_path} does not contain expected database name.")

        print(f'Backup file {backup_file_path} is valid and contains data for {DB_NAME}.')

    except FileNotFoundError as e:
        print(f'Error: {e}')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


if __name__ == '__main__':
    check_backup()
