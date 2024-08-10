import subprocess
import datetime
import os

# MySQL database configuration
DB_HOST = 'localhost'  # Replace with your database host
DB_USER = 'ubuntu'  # Replace with your database username
DB_PASSWORD = 'uwunyanichan'  # Replace with your database password
DB_NAME = 'ttranking'  # Replace with your database name

# Backup configuration
BACKUP_DIR = os.path.expanduser('~/backups/')
TIMESTAMP = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
BACKUP_FILE = os.path.join(BACKUP_DIR, f'{DB_NAME}_{TIMESTAMP}.sql')


# Create the backup
def create_backup():
    try:
        # Command to execute
        cmd = [
            'mysqldump',
            '-h', DB_HOST,
            '-u', DB_USER,
            '-p' + DB_PASSWORD,
            DB_NAME
        ]

        # Open the backup file for writing
        with open(BACKUP_FILE, 'wb') as f:
            subprocess.run(cmd, stdout=f, check=True)

        print(f'Backup successfully created at {BACKUP_FILE}')
    except subprocess.CalledProcessError as e:
        print(f'Error during backup: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    create_backup()
