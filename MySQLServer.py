#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

# Replace with your MySQL username and password
DB_USER = "root"
DB_PASSWORD = "Abadaniel@284"
DB_HOST = "localhost"
DATABASE_NAME = "alx_book_store"

def create_database():
    """Creates the alx_book_store database if it does not exist."""
    try:
        # Establish connection to the MySQL server
        cnx = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = cnx.cursor()

        # SQL statement to create the database
        create_db_query = "CREATE DATABASE IF NOT EXISTS {}".format(DATABASE_NAME)

        # Execute the SQL statement
        cursor.execute(create_db_query)

        print("Database '{}' created successfully!".format(DATABASE_NAME))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error: {}".format(err))
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()