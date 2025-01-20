import re
import os

# Define the MySQL dump file path and output file path
mysql_dump_file = '../backups/ttranking.sql'
postgres_dump_file = '../backups/converted_postgres.sql'

def convert_mysql_to_postgres(mysql_dump_file, postgres_dump_file):
    try:
        with open(mysql_dump_file, 'r') as infile, open(postgres_dump_file, 'w') as outfile:
            sql_content = infile.read()

            # 1. Remove ENGINE=InnoDB specification (not needed in PostgreSQL)
            sql_content = re.sub(r'ENGINE=[^;]+;', '', sql_content)

            # 2. Replace AUTO_INCREMENT with SERIAL
            sql_content = re.sub(r'\bAUTO_INCREMENT\b', 'SERIAL', sql_content)

            # 3. Replace MySQL data types with PostgreSQL equivalents
            sql_content = sql_content.replace('TINYINT', 'SMALLINT')
            sql_content = sql_content.replace('MEDIUMINT', 'INTEGER')
            sql_content = sql_content.replace('DATETIME', 'TIMESTAMP')
            sql_content = sql_content.replace('longtext', 'TEXT')

            # 4. Replace backticks with double quotes for PostgreSQL
            sql_content = re.sub(r'`([^`]+)`', r'"\1"', sql_content)

            # 5. Replace NOW() with CURRENT_TIMESTAMP
            sql_content = sql_content.replace('NOW()', 'CURRENT_TIMESTAMP')

            # 6. Replace CONCAT() with PostgreSQL CONCAT()
            sql_content = sql_content.replace('CONCAT(', 'CONCAT(')

            # 7. Remove MySQL-specific table locking commands
            sql_content = re.sub(r'LOCK TABLES.*?;', '', sql_content, flags=re.DOTALL)
            sql_content = sql_content.replace('UNLOCK TABLES;', '')

            # 8. Handle SERIAL syntax correctly
            sql_content = sql_content.replace('int NOT NULL SERIAL', 'SERIAL PRIMARY KEY')

            # Write the converted content to the output file
            outfile.write(sql_content)
            print(f"Conversion complete! The PostgreSQL compatible dump is saved at {postgres_dump_file}.")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    convert_mysql_to_postgres(mysql_dump_file, postgres_dump_file)
