CREATE DATABASE sql_projects;
SHOW DATABASES;
USE sql_projects;
CREATE TABLE songs (
    track_id VARCHAR(80),
    track_name VARCHAR(1000),
    track_artist VARCHAR(600),
    track_popularity VARCHAR(20),
    track_album_id VARCHAR(100),
    track_album_name VARCHAR(1000),track_album_release_date VARCHAR(40),
    playlist_name VARCHAR(2000),
    playlist_id VARCHAR(600),
    playlist_genre VARCHAR(200),
    playlist_subgenre VARCHAR(290),
    danceability DECIMAL(10,3),
    energy DECIMAL(10,3),
    _key INT,
    loudness DECIMAL(10,3),
    mode DECIMAL(10,3),
    speechiness DECIMAL(10,3),
    acousticness DECIMAL(10,3),
    instrumentalness DECIMAL(10,3),
    liveness DECIMAL(10,3),
    valence DECIMAL(10,3),
    tempo DECIMAL(10,3),
    duration_ms BIGINT
);
DROP TABLE songs;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/spotify_songs.csv'
INTO TABLE songs
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SELECT * FROM songs;