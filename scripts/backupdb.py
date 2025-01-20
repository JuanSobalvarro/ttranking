# ttranking/backupdb.py
import subprocess
import datetime
import os

# PostgreSQL database configuration
DB_HOST = 'localhost'  # Replace with your database host
DB_USER = 'root'  # Replace with your database username
DB_PASSWORD = 'uwunyanichan'  # Replace with your database password
DB_NAME = 'ttranking'  # Replace with your database name
DB_PORT = '5432'  # Default PostgreSQL port

# Backup configuration
BACKUP_DIR = os.path.expanduser('../backups/')
os.makedirs(BACKUP_DIR, exist_ok=True)  # Ensure the backup directory exists
TIMESTAMP = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
BACKUP_FILE = os.path.join(BACKUP_DIR, f'{DB_NAME}_{TIMESTAMP}.sql')

# Create the backup
def create_backup():
    try:
        # Set the password in the environment
        os.environ['PGPASSWORD'] = DB_PASSWORD

        # Command to execute
        cmd = [
            'pg_dump',
            '-h', DB_HOST,
            '-U', DB_USER,
            '-p', DB_PORT,
            '-F', 'c',  # Custom format for better compression and flexibility
            '-f', BACKUP_FILE,  # Output file
            DB_NAME
        ]

        # Run the command
        subprocess.run(cmd, check=True)

        print(f'Backup successfully created at {BACKUP_FILE}')
    except subprocess.CalledProcessError as e:
        print(f'Error during backup: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Remove PGPASSWORD from the environment for security
        os.environ.pop('PGPASSWORD', None)


if __name__ == '__main__':
    create_backup()
