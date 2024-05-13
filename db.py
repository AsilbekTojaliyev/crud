import sqlite3
from sqlite3 import connect


def get_db_connection():
    conn = None
    try:
        conn = connect("data.db")
        return conn
    except sqlite3.Error as e:
        print(e)
