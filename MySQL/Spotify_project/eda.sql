USE music_analysis_project;

-- How many tracks and playlists?
SELECT COUNT(*) AS total_records, 
    COUNT(DISTINCT track_id) AS unique_tracks,
    COUNT(DISTINCT playlist_id) AS unique_playlist
FROM cleaned_tracks;

-- Which genres have the most tracks?
SELECT
    playlist_genre, COUNT(*) AS track_count
FROM cleaned_tracks
GROUP BY playlist_genre
ORDER BY track_count DESC;

-- Which subgenres have the most tracks?
SELECT
    playlist_subgenre, COUNT(*) AS track_count
FROM cleaned_tracks
GROUP BY playlist_subgenre
ORDER BY track_count DESC;

-- What are the most popular tracks?
SELECT track_name, track_artist, track_popularity, playlist_genre
FROM cleaned_tracks
ORDER BY track_popularity DESC
LIMIT 20;

-- Which artists have the most tracks?
SELECT track_artist, COUNT(DISTINCT track_id) AS unique_tracks
FROM cleaned_tracks
GROUP BY track_artist
ORDER BY unique_tracks DESC
LIMIT 20;

-- Which genres have the highest popularity?
SELECT
    playlist_genre,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity,
    MAX(track_popularity) AS max_popularity
FROM cleaned_tracks
GROUP BY playlist_genre
ORDER BY avg_popularity DESC;

-- Does energy relate to popularity?
SELECT
    energy_level,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
GROUP BY energy_level
ORDER BY avg_popularity DESC;

-- Short vs medium vs long tracks
SELECT
    duration_category,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
GROUP BY duration_category
ORDER BY avg_popularity DESC;

-- Popularity by release year
SELECT
    release_year,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year;

-- Which artists have the highest average popularity?
SELECT
    track_artist,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
GROUP BY track_artist
HAVING COUNT(DISTINCT track_id) >= 5
ORDER BY avg_popularity DESC
LIMIT 20;