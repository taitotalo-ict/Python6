import sqlite3
from pathlib import Path

BASEDIR = Path(__file__).parent

db = BASEDIR / 'mytest.sqlite'
if not db.exists():
    raise Exception('Database file is not found')

conn = sqlite3.connect(db)
cursor = conn.cursor()

nimi = input('Etunimi? ')

# cursor.execute(f"SELECT * FROM users WHERE etunimi='{nimi}'") # SQL inyection!!!
cursor.execute("SELECT * FROM users WHERE etunimi=?", (nimi,))
for row in cursor:
    print(row)