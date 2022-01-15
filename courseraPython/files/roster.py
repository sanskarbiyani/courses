import json
import sqlite3

conn = sqlite3.connect("rostersql.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE Users(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
)
''')

fname = input("Enter filename: ")
if len(fname) < 1: fname = "roster_data.json"

content = open(fname).read()
fulldata = json.loads(content)
print("NAME \t  COURSE \t ROLE")

for data in fulldata:
    name = data[0]
    course = data[1]
    role = data[2]

    print(name + "\t   " + course + "\t   " + str(role))

    cur.execute('INSERT OR IGNORE INTO Users(name) VALUES (?)', (name, ))
    cur.execute('SELECT id FROM Users WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (course, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

    conn.commit()
