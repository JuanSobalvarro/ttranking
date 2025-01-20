import os
import subprocess

# Configuration
POSTGRES_CONTAINER_NAME = "ttranking-db-1"  # Replace with your PostgreSQL container name
DUMP_FILE_PATH = "../backups/converted_postgres.sql"  # Replace with the path to your PostgreSQL dump file
POSTGRES_USER = "root"  # Replace with your PostgreSQL user
POSTGRES_DB = "ttranking"  # Replace with your database name

# Helper function to execute a shell command
def run_command(command):
    """Executes a shell command."""
    try:
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"stderr: {e.stderr}")
        return None

# Step 1: Copy the dump file to the PostgreSQL container
def copy_dump_to_container():
    print(f"Copying dump file to PostgreSQL container: {POSTGRES_CONTAINER_NAME}")
    command = ["docker", "cp", DUMP_FILE_PATH, f"{POSTGRES_CONTAINER_NAME}:/tmp/dump.sql"]
    result = run_command(command)
    if result is not None:
        print(f"Successfully copied dump file to {POSTGRES_CONTAINER_NAME}.")
        return True
    return False

# Step 2: Load the dump into the PostgreSQL database
def load_dump_into_postgres():
    print(f"Loading dump into PostgreSQL database in container: {POSTGRES_CONTAINER_NAME}")
    command = [
        "docker", "exec", POSTGRES_CONTAINER_NAME,
        "psql", "-U", POSTGRES_USER, "-d", POSTGRES_DB, "-f", "/tmp/dump.sql"
    ]
    result = run_command(command)
    if result is not None:
        print(f"Successfully loaded dump into PostgreSQL database.")
        return True
    return False

# Step 3: Apply migrations
def apply_migrations():
    print("Applying migrations...")
    command = ["docker", "exec", POSTGRES_CONTAINER_NAME, "sh", "-c", "pg_dump", "-U", POSTGRES_USER ,"> /tmp/post_migrations.sql"]
    result = run_command(command)
    if result is not None:
        print("Migrations applied successfully.")
        return True
    return False

# Step 4: Cleanup
def cleanup():
    print("Cleaning up temporary files...")
    command = ["docker", "exec", POSTGRES_CONTAINER_NAME, "rm", "/tmp/dump.sql"]
    run_command(command)
    print("Cleanup complete.")

def main():
    # Check if dump file exists
    if not os.path.exists(DUMP_FILE_PATH):
        print(f"Error: Dump file {DUMP_FILE_PATH} does not exist.")
        return

    # Step 1: Copy the dump file to the container
    if not copy_dump_to_container():
        return

    # Step 2: Load the dump into PostgreSQL
    if not load_dump_into_postgres():
        return

    # Step 3: Apply migrations
    if not apply_migrations():
        return

    # Step 4: Cleanup temporary files
    cleanup()

if __name__ == "__main__":
    main()
