import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input("Enter Filename: ")
if len(fname) < 1: fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
     if not line.startswith('From: '): continue
     peices = line.split()
     email = peices[1]
     cur.execute('SELECT Count FROM Counts WHERE email = ?', (email, ))
     row = cur.fetchone()
     if row is None:
        # ? So to prevent code injection in our sql database. ? will be replaced by the value in the email variable
        # THe values are passed as a tupple and they must be equal to the number of ?
        # The value will be replaced in order
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email, ))
     else:
        cur.execute('UPDATE Counts SET Count = Count+1 WHERE email = ?', (email, ))
     conn.commit()

# DESC is discending and we are limit the output by using LIMIT
sqlstr = 'SELECT email, Count FROM Counts ORDER BY Count DESC LIMIT 10' # We can use * instead of email,count as the table contains only 2 columns

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
