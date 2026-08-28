DROP DATABASE sql_projects;
SHOW DATABASES;
CREATE DATABASE music_analysis_project;
USE music_analysis_project;
CREATE TABLE raw_tracks (
    track_id VARCHAR(100),
    track_name TEXT,
    track_artist TEXT,
    track_popularity INT,
    track_album_id VARCHAR(100),
    track_album_name TEXT,
    track_album_release_date VARCHAR(20),
    playlist_name TEXT,
    playlist_id VARCHAR(100),
    playlist_genre VARCHAR(50),
    playlist_subgenre VARCHAR(100),
    danceability DECIMAL(5,4),
    energy DECIMAL(5,4),
    `key` INT,
    loudness DECIMAL(6,3),
    mode INT,
    speechiness DECIMAL(5,4),
    acousticness DECIMAL(5,4),
    instrumentalness DECIMAL(5,4),
    liveness DECIMAL(5,4),
    valence DECIMAL(5,4),
    tempo DECIMAL(8,3),
    duration_ms INT
);