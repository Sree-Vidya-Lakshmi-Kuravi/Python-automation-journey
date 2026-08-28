USE music_analysis_project;
SHOW VARIABLES LIKE 'local_infile';
LOAD DATA LOCAL INFILE 'E:/Vidya Career/IT JOB/Repati Kosam/MySQL/Spotify_project/spotify_songs.csv'
INTO TABLE raw_tracks
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SELECT COUNT(*) FROM raw_tracks;
DESCRIBE raw_tracks;