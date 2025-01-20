#!/bin/bash

# Configuration
SQL_FILE_PATH="/scripts/ttranking.sql"  # Path to the .sql file inside the container
POSTGRES_USER="root"                   # PostgreSQL user
POSTGRES_DB="ttranking"                # PostgreSQL database name

# Check if the SQL file exists
if [ ! -f "$SQL_FILE_PATH" ]; then
    echo "Error: SQL file not found at $SQL_FILE_PATH"
    exit 1
fi

# Execute the SQL file using psql
echo "Loading data from $SQL_FILE_PATH into the PostgreSQL database: $POSTGRES_DB..."
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f "$SQL_FILE_PATH"
if [ $? -ne 0 ]; then
    echo "Error: Failed to load data into the PostgreSQL database."
    exit 1
fi

echo "Data successfully imported into PostgreSQL."
