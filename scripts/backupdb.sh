#!/bin/bash

# PostgreSQL database configuration
DB_HOST="localhost"      # Replace with your database host
DB_USER="root"           # Replace with your database username
DB_PASSWORD="uwunyanichan"  # Replace with your database password
DB_NAME="ttranking"      # Replace with your database name
DB_PORT="5432"           # Default PostgreSQL port

# Backup configuration
BACKUP_DIR="../backups"  # Replace with your backup directory path
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/${DB_NAME}_${TIMESTAMP}.sql"

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Export the password to the environment for pg_dump
export PGPASSWORD="$DB_PASSWORD"

# Create the backup
echo "Starting backup for database '$DB_NAME'..."
if pg_dump -h "$DB_HOST" -U "$DB_USER" -p "$DB_PORT" -F c -f "$BACKUP_FILE" "$DB_NAME"; then
    echo "Backup successfully created at $BACKUP_FILE"
else
    echo "Error occurred during backup."
    exit 1
fi

# Unset the password for security
unset PGPASSWORD

# Finish
echo "Backup process completed."
