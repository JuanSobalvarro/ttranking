#!/bin/bash

# PostgreSQL database configuration
DB_HOST="localhost"      # Replace with your database host
DB_USER="root"           # Replace with your database username
DB_PASSWORD="uwunyanichan"  # Replace with your database password
DB_NAME="ttranking"      # Replace with your database name
DB_PORT="5432"           # Default PostgreSQL port

# Dump file configuration
DUMP_FILE="$1"  # Pass the dump file path as the first argument to the script

# Check if a dump file is provided
if [ -z "$DUMP_FILE" ]; then
    echo "Usage: $0 <path_to_dump_file>"
    exit 1
fi

# Check if the dump file exists
if [ ! -f "$DUMP_FILE" ]; then
    echo "Error: Dump file '$DUMP_FILE' does not exist."
    exit 1
fi

# Export the password to the environment for psql
export PGPASSWORD="$DB_PASSWORD"

# Restore the database
echo "Starting restore for database '$DB_NAME' from dump file '$DUMP_FILE'..."
if pg_restore -h "$DB_HOST" -U "$DB_USER" -p "$DB_PORT" -d "$DB_NAME" --clean --if-exists "$DUMP_FILE"; then
    echo "Database '$DB_NAME' successfully restored from '$DUMP_FILE'."
else
    echo "Error occurred during database restoration."
    exit 1
fi

# Unset the password for security
unset PGPASSWORD

# Finish
echo "Restore process completed."
