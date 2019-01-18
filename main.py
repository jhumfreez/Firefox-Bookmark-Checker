import requests
from location import getLocation
import requests
import sqlite3
import os

def getStatus(url):
    status = 0
    try:
        r = requests.get(url)
        status = r.status_code
    except Exception as e:
        print("Error for "+url)
        print(str(e))
    return status


def testurl(url):
    if url[:4] != 'http':
        return
    status = getStatus(url)
    if status != 200 and status != 401:
        msg = "Link failed {0}\n\t with code {1}".format(url, status)
        print(msg)
        with open('output.log', 'a') as f:
            f.write(msg+'\n\n')


def connect(db_path):
    # loop rows, get url, test url
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # get list of not null fk from moz_bookmarks, query the url from moz_places where id = fk and url[:4] = "http"
    query = """SELECT moz_places.url as url
                FROM moz_places
                JOIN moz_bookmarks ON moz_places.id = moz_bookmarks.fk
                WHERE moz_bookmarks.fk NOT NULL"""
    c.execute(query)
    # get rows
    results = c.fetchall()
    for url_tuple in results:
        testurl(url_tuple[0])


def main():
    getLocation()
    db_path = os.environ['DB_PATH']
    connect(db_path)


if __name__ == "__main__":
    main()
