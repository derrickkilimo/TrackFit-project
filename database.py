# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./fitness.db"

# engine = create_engine(DATABASE_URL)
# Base = declarative_base()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# database.py

import sqlite3

def connect_to_database(database_file):
    """
    Create a connection to the SQLite database.
    
    Args:
        database_file (str): The name of the SQLite database file.
    
    Returns:
        sqlite3.Connection: A connection to the database.
    """
    try:
        connection = sqlite3.connect(database_file)
        print("Connected to the database")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_cursor(connection):
    """
    Create a cursor for executing SQL statements on the database connection.
    
    Args:
        connection (sqlite3.Connection): A connection to the database.
    
    Returns:
        sqlite3.Cursor: A cursor object.
    """
    if connection:
        return connection.cursor()
    else:
        return None

def create_user_table(cursor):
    """
    Create a 'user' table in the database.
    
    Args:
        cursor (sqlite3.Cursor): A cursor for executing SQL statements.
    """
    if cursor:
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            email TEXT
        )
        """
        cursor.execute(create_table_sql)
        print("User table created")
    else:
        print("Cursor is not available")

def insert_user(cursor, username, email):
    """
    Insert a new user into the 'user' table.
    
    Args:
        cursor (sqlite3.Cursor): A cursor for executing SQL statements.
        username (str): The username of the user.
        email (str): The email address of the user.
    """
    if cursor:
        insert_sql = "INSERT INTO user (username, email) VALUES (?, ?)"
        cursor.execute(insert_sql, (username, email))
        print("User inserted successfully")
    else:
        print("Cursor is not available")

def fetch_users(cursor):
    """
    Fetch all users from the 'user' table.
    
    Args:
        cursor (sqlite3.Cursor): A cursor for executing SQL statements.
    
    Returns:
        list: A list of user records (tuples).
    """
    if cursor:
        cursor.execute("SELECT * FROM user")
        return cursor.fetchall()
    else:
        print("Cursor is not available")
        return []

def close_database(connection):
    """
    Close the database connection.
    
    Args:
        connection (sqlite3.Connection): A connection to the database.
    """
    if connection:
        connection.commit()
        connection.close()
        print("Database connection closed")
    else:
        print("Connection is not available")

# You can add more functions for other database operations as needed

