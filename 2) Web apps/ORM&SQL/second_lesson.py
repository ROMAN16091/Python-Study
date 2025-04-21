import sqlite3, re

conn = sqlite3.connect('my_database.db')

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users
(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT,
    age   INTEGER,
    email TEXT UNIQUE
)
''')


cur.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', ('Ivan', 30, 'ivan@example,com'))

users = [
    ('Bob', 25, 'bob@example.com'),
    ('Alice', 28, 'alice@example.com')
]

cur.executemany('INSERT INTO users (name,age, email) VALUES (?,?,?)', users)

cur.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'IVAN'))

cur.execute('DELETE FROM users WHERE age < ?', (26,))

conn.commit()

cur.execute('SELECT * FROM users')

rows = cur.fetchall()
for row in rows:
    print(row)

user1 = cur.fetchone()
user2 = cur.fetchone()
user3 = cur.fetchone()
print(user1)
print(user2)
print(user3)

users = [
    ('Ira', 23, 'ira@example.com'),
    ('Igor', 22, 'igor@example.com')
]

cur.executemany('INSERT INTO users (name,age, email) VALUES (?,?,?)', users)

conn.commit()

# cur.execute('SELECT * FROM users WHERE')
#
# users_result = cur.fetchmany(10)
# print(users_result)

def regexp(pattern, string):
    return re.search(pattern,string) is not None

conn.create_function('REGEXP', 2, regexp)
cur.execute('SELECT * FROM users WHERE name REGEXP ?', ('^B',))
users_I =cur.fetchall()
for user in users:
    print(user)

cur.close()
conn.close()
