import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates the alx_book_store database if it doesn't exist"""
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='TatsLove',
            password='m200936577J03*'
        )
        
        # Create cursor and execute CREATE DATABASE statement
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database created successfully")

    except Error as err:
        # Handle MySQL-specific errors
        print(f"MySQL Error: {err}")
    except Exception as err:
        # Handle other exceptions
        print(f"Error occurred: {err}")
    finally:
        # Clean up resources
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
