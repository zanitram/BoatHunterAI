import sqlite3

DATABASE = "data/boats.db"

def connect():
    return sqlite3.connect(DATABASE)

def initialize():

    conn = connect()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS boats(

            id INTEGER PRIMARY KEY,

            name TEXT,

            price INTEGER,

            location TEXT,

            engine TEXT,

            length REAL,

            trailer INTEGER,

            score INTEGER,

            notes TEXT

        )
    """)

    conn.commit()
    conn.close()