import sqlite3
import urllib.error
import ssl
from urllib.parse import url.join
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("spider.sqlite")
cur = conn.cursor()

cur.executescript(
'''
    CREATE TABLE IF NOT EXISTS Pages
        (id INTEGER PRIMARY KEY, url TEXT, html TEXT,
        error INTEGER, old_rank REAL, new_rank REAL);

    CREATE TABLE IF NOT EXISTS Links
        (from_id INTEGER, to_id INTEGER,
        UNIQUE(from_id, to_id)
        );

    CREATE TABLE IF NOT EXISTS Webs
        (url TEXT UNIQUE)
'''
)

# Checking if the the Webs table consists of a web, if present restart the crawl
cur.execute(''' SELECT id, url FROM PAGES WHERE html IS NULL AND ERROR IS NULL ORDER BY RANDOM() LIMIT 1''')
cur.fetchone()
if row is not None:
    print("Restarting crawl, For new crawl delete spyder.sqlite file")
else:
    # Inputing the website from the user and checking that there are no errors, if present removing them
    # the following block is checking and correcting the website name
    start_url = input("Enter the url or Enter: ")
    if len(start_url) < 1: start_url = "http://dr-chuck.com/"
    if start_url.endswith('/'): start_url = start_url[:-1]
    web = start_url
    if start_url.endswith('.htm') or start_url.endswith('.html'):
        pos = start_url.rfind('/')
        web = start_url[:pos]
    if len(start_utl) > 1:
        cur.execute("INSERT INTO Webs(url) VALUES (?)", ( web,)) # Domain
        cur.execute("INSERT INTO Pages(url, html, new_rank) VALUES (?, NULL, 1.0)", ( start_url,)) # Home Page
        conn.commit()

cur.execute("SELECT url FROM Webs")
webs = list()
for row in cur:
    webs.append(str([0]))
print(webs)

many = 0
while True:
    if (many < 1):
        val = input("How many pages: ")
        if len(val) < 1: break
        many = int(val)
    many -= 1
    # Picking up a random page in the website
    cur.execute("SELECT id, url FROM Pages WHERE html IS NULL AND ERROR IS NULL ORDER BY RANDOM() LIMIT 1")
    try:
        row = cur.fetchone()
        fromid = row[0]
        url = row[1]
    except:
        print("No unretrived Pages")
        many = 0
        break

    print("Retreiving: ", from_id, url, end = " ")
    # the database should not consists of the from links as it has not been parsed
    cur.execute("DELETE FROM Links WHERE from_id = ?", ( from_id,))
    # Retreiving the webpage
    try:
        # opening the page picked and seeing if that was retreived successfully
        data = urlopen(url, context=ctx)
        html = document.read()
        if data.getcode() != 200: # Checking if the page was retreived successfully or not by the error code
            print("Error in opening of the pages", data.getcode())
            cur.execute("UPDATE Pages SET error = ? WHERE url = ?", (data.getcode(), url))
        if "text/html" != data.info().get_content_type(): # Checking the type of content of the page
            print("Ignoring Pages that are not html/text type")
            cur.execute("DELETE FROM Pages WHERE url = ?", ( url,))
            conn.commit()
            continue

        print('(' + str(len(html)) + ')', end = " ")
        soup = BeautifulSoup(html, "html.parser")
    except KeyboardInterrupt:
        print(" ")
        print("Program interrupted by user....")
        break
    except:
        print("Unable to retreive the page.")
        cur.execute("UPDATE Pages SET error = -1 WHERE url =? ", ( url,))
        break

    # We need two lines instead of 1 because the present pages needs to be updates whereas new pages need to be added, both cannot be done in the same line
    cur.execute("INSERT OT IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)", (url,))
    cur.execute("UPADTE Pages SET html = ? WHERE url = ?", (memoryview(html)), url)
    conn.commit()

    # To get the links present in the page
    tags = soup('a')
    count = 0
    # Going link ny link
    for tag in tags:
        href = tag.get('href', None)
        if href is None: continue
        up = urlparse(href) # parding is seaprating the links into its components
        if len(up.scheme) < 1:href = urljoin(url, href) # scheme = "HTTPS" Or some other like that
        ipos = href.find('#') # To remove the fragments(points to certain part in the page)
        if ipos > 1: href = href[:ipos]
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'): continue
        if href.endswith('/') : href = href[:-1] # Removing the last slash
        if len(href) < 1: continue

        # To check if the page found is of the same website or not
        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found: continue

        # Insert the page in the table as unretreived
        cur.execute("INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES (?, NULL, 1.0)", ( href,))
        count +=1
        conn.commit()

        # To get the id of the row that the page is present into
        cur.execute("SELECT id FROM Pages WHERE url = ?", ( href,))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print("Could not retreive id")
            continue

        cur.execute("INSERT OR IGNORE INTO Links (from_id, to_id) VALUES (?, ?)", (fromid, toid))

    print(count)

cur.close()
