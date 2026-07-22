import sqlite3
from pathlib import Path

DATABASE = "data/boats.db"


def connect():
    database_path = Path(DATABASE)
    database_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(database_path)


def initialize():
    conn = connect()

    conn.execute(
        """
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
        """
    )

    conn.commit()
    conn.close()


def add_boat(boat):
    conn = connect()

    cursor = conn.execute(
        """
        INSERT INTO boats
        (name,price,location,engine,length,trailer,score,notes)
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            boat.name,
            boat.price,
            boat.location,
            boat.engine,
            boat.length,
            int(boat.trailer),
            boat.score,
            boat.notes,
        ),
    )

    conn.commit()
    boat_id = cursor.lastrowid
    conn.close()
    return boat_id


def update_boat(boat_id, **fields):
    if not fields:
        return None

    assignments = ", ".join(f"{field}=?" for field in fields)
    values = list(fields.values()) + [boat_id]

    conn = connect()
    conn.execute(f"UPDATE boats SET {assignments} WHERE id=?", values)
    conn.commit()
    conn.close()
    return boat_id


def get_boat(boat_id):
    conn = connect()
    row = conn.execute(
        """
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
        WHERE id=?
        """,
        (boat_id,),
    ).fetchone()
    conn.close()
    return row


def get_boats():
    conn = connect()

    rows = conn.execute(
        """
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
        ORDER BY score DESC, price ASC
        """
    ).fetchall()

    conn.close()
    return rows


def delete_boat(boat_id):
    conn = connect()
    conn.execute("DELETE FROM boats WHERE id=?", (boat_id,))
    conn.commit()
    conn.close()


def get_dashboard_stats():
    conn = connect()
    row = conn.execute(
        """
        SELECT
            COUNT(*) AS total_boats,
            AVG(score) AS average_score,
            AVG(price) AS average_price,
            MAX(score) AS top_score
        FROM boats
        """
    ).fetchone()
    conn.close()

    total_boats = row[0] or 0
    average_score = round(row[1] or 0, 1)
    average_price = round(row[2] or 0, 2)
    top_score = row[3] or 0

    return {
        "total_boats": total_boats,
        "average_score": average_score,
        "average_price": average_price,
        "top_score": top_score,
    }