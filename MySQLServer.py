import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='TatsLove',
            password='m200936577J03*'
        )

        cursor = connection.cursor()
        # Only using CREATE DATABASE, no SELECT or SHOW statements
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL or creating database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
