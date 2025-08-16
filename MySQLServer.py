import mysql.connector
from mysql.connector import errorcode

# ... (rest of your script) ...

def create_database():
    """Creates the alx_book_store database if it does not exist."""
    try:
        # Establish connection to the MySQL server
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abadaniel@284"
        )
        
        cursor = cnx.cursor()

        # The SQL statement to create the database
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the SQL statement
        cursor.execute(create_db_query)

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        else:
            print("Error: {}".format(err))
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()