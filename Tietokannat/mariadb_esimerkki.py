import mariadb

conn = mariadb.connect(
    user = 'root',
    password = '',
    database = 'test',
    # host = '127.0.0.1',
    # port = 3306,
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute('CREATE DATABASE ')

cursor.execute('CREATE TABLE IF NOT EXISTS users (etunimi VARCHAR(100), sukunimi VARCHAR(100), email VARCHAR(100))')

cursor.execute('INSERT INTO users VALUES ("Christian", "Finnberg", "christian.finnberg@taitotalo.fi")')

cursor.execute('SELECT * FROM users')
for row in cursor:
    print(row)

conn.close()