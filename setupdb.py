# ttranking/setupdb.py
import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import errorcode

load_dotenv(dotenv_path='ttranking/.env')


# Database configuration
config = {
    'user': os.getenv('DB_USER'),  # MySQL root user
    'password': os.getenv('DB_PASS'),  # MySQL root password
    'host': 'localhost',  # MySQL server host
    'port': 3306,
}

# Database and user details
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASS')

print('Using:', f'db_name={db_name}, db_user={db_user}, db_password={db_password}')


def main():
    cursor = None
    cnx = None
    # Connect to MySQL server
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        print("Connected to MySQL server.")

        # Create database
        try:
            cursor.execute(f"CREATE DATABASE {db_name} DEFAULT CHARACTER SET 'utf8'")
            print(f"Database '{db_name}' created successfully.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Database '{db_name}' already exists.")
            else:
                print(err.msg)

        # Create user and grant privileges
        try:
            cursor.execute(f"CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_password}'")
            print(f"User '{db_user}' created successfully.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_CANNOT_USER:
                print(f"User '{db_user}' already exists.")
            else:
                print(err.msg)

        try:
            cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost'")
            cursor.execute("FLUSH PRIVILEGES")
            print(f"Granted all privileges on '{db_name}' to '{db_user}'.")
        except mysql.connector.Error as err:
            print(err.msg)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close connection
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()
        print("Connection closed.")


if __name__ == '__main__':
    main()
