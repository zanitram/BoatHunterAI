import sqlite3

DATABASE = "data/boats.db"


def connect():
    return sqlite3.connect(DATABASE)


def initialize():
    conn = connect()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS boats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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


def add_boat(boat):
    conn = connect()

    conn.execute("""
        INSERT INTO boats
        (name,price,location,engine,length,trailer,score,notes)
        VALUES(?,?,?,?,?,?,?,?)
    """, (
        boat.name,
        boat.price,
        boat.location,
        boat.engine,
        boat.length,
        int(boat.trailer),
        boat.score,
        boat.notes
    ))

    conn.commit()
    conn.close()


def get_boats():

    conn = connect()

    rows = conn.execute("""
        SELECT
            id,
            name,
            price,
            location,
            engine,
            length,
            trailer,
            score,
            notes
        FROM boats
        ORDER BY score DESC
    """).fetchall()

    conn.close()

    return rows


def delete_boat(id):

    conn = connect()

    conn.execute(
        "DELETE FROM boats WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()