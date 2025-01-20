import mysql.connector
import csv
import os

def export_tables_to_csv():
    # MySQL connection configuration
    MYSQL_HOST = 'localhost'  # MySQL host
    MYSQL_USER = 'root'  # MySQL user
    MYSQL_PASSWORD = 'uwunyanichan'  # MySQL password
    MYSQL_DB = 'ttranking'  # Database name

    # Create a folder to save the CSV files
    output_folder = 'mysql_csv'
    os.makedirs(output_folder, exist_ok=True)

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    cursor = connection.cursor()

    # Get all table names from the database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Loop through each table and export it to CSV
    for table in tables:
        table_name = table[0]
        print(f"Exporting table: {table_name}")

        # Fetch all rows from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Get column names (headers) from the table
        columns = [column[0] for column in cursor.description]

        # Define CSV file path
        csv_file_path = os.path.join(output_folder, f"{table_name}.csv")

        # Write rows to CSV
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write the header (column names)
            writer.writerows(rows)  # Write all data rows

        print(f"Table {table_name} exported to {csv_file_path}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

    print("Data export complete.")

def main():
    export_tables_to_csv()

if __name__ == '__main__':
    main()
