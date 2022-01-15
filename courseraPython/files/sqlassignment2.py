import sqlite3

conn = sqlite3.connect('assignment2database.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
fh = open('mbox.txt')

for line in fh:
    if not line.startswith('From: '): continue
    peices = line.split()
    org = peices[1].split('@')[1]
    cur.execute('SELECT Count FROM Counts WHERE org=?', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))
    else:
        cur.execute('UPDATE Counts SET Count = Count + 1 WHERE org = ?', (org, ))
    conn.commit()

conn.close()
