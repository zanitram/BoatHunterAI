import sqlite3
DB="data/boats.db"
def initialize():
    con=sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS boats(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,price INTEGER,location TEXT,engine TEXT,
    length REAL,trailer INTEGER,score INTEGER,notes TEXT)""")
    con.commit(); con.close()
