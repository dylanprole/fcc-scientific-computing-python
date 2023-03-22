DROP TABLE IF EXISTS Library;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	name TEXT,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Artist
    (name)
VALUES
	('Linkin Park'),
	('Ed Sheeran');

CREATE TABLE Album (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	artist_id INTEGER REFERENCES Artist(id),
	title TEXT,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Album 
    (title, artist_id) 
VALUES
    ('Hybrid Theory', 1),
	('Meteora', 1),
    ('+', 2),
    ('x', 2);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name TEXT,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Genre 
    (name)
VALUES
    ('Pop'),
    ('Rock');

CREATE TABLE Track (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    title TEXT,
    album_id INTEGER REFERENCES Album(id),
    genre_id INTEGER REFERENCES Genre(id),
    len INTEGER, rating INTEGER, count INTEGER,
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Track
    (title, album_id, genre_id, len, rating, count)
VALUES
    ('Crawling', 1, 1, 216, 5, 21),
    ('Breaking the Habit', 2, 1, 196, 5, 52),
    ('The A Team', 3, 2, 258, 3, 8),
    ('Bloodstream', 4, 2, 300, 2, 5);

CREATE TABLE Library AS
    SELECT  
        Track.title AS track,
        cast(Track.len / 60  as TEXT) || ':' || cast(Track.len % 60 AS TEXT) AS length,
        Artist.name AS artist,
        Album.title AS album,
        Genre.name AS genre,
        printf('%.*c', Track.rating, '★') AS rating,
        Track.count AS count
    FROM Track
    JOIN Album
        ON Track.album_id = Album.id
    JOIN Artist
        ON Album.artist_id = Artist.id
    JOIN Genre 
        ON Track.genre_id = Genre.id;

SELECT * FROM Library;