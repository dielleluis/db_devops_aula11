import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS albums(
                albumId integer PRIMARY KEY,
                title text NOT NULL,
                artistId integer NOT NULL,
                FOREIGN KEY (artistId) REFERENCES artist)''')

c.execute('''CREATE TABLE IF NOT EXISTS artist(
                artistId integer PRIMARY KEY,
                name text NOT NULL)''')

c.execute(" INSERT INTO albums (albumId, title, artistId) VALUES(1, 'THE WALL', 100)")
c.execute(" INSERT INTO albums (albumId, title, artistId) VALUES(2, 'BAND OF GYPSYS', 200)")
c.execute(" INSERT INTO albums (albumId, title, artistId) VALUES(3, 'HOTEL CALIFORNIA', 300)")
c.execute(" INSERT INTO artist (artistId, name) VALUES(100, 'PINKY FLOYD')")
c.execute(" INSERT INTO artist (artistId, name) VALUES(200, 'JIMI HENDRIX')")
c.execute(" INSERT INTO artist (artistId, name) VALUES(300, 'EAGLES')")

c.execute("SELECT Title, Name FROM albums INNER JOIN artist ON artist.artistId = albums.artistId")

conn.commit()
conn.close()