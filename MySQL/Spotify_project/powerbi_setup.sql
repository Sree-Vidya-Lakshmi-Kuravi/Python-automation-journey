CREATE OR REPLACE VIEW analysis_tracks AS
SELECT * FROM cleaned_tracks;

SELECT * FROM analysis_tracks LIMIT 10;
SELECT COUNT(*) AS total_rows FROM analysis_tracks;

-- Check the view structure
DESCRIBE analysis_tracks;

-- Create a genre summary view
CREATE OR REPLACE VIEW genre_summary AS
SELECT
    playlist_genre,
    COUNT(DISTINCT track_id) AS unique_tracks,
    COUNT(DISTINCT playlist_id) AS unique_playlists,
    ROUND(AVG(track_popularity), 2) AS avg_popularity,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    ROUND(AVG(energy), 3) AS avg_energy,
    ROUND(AVG(valence), 3) AS avg_valence,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes
FROM cleaned_tracks
GROUP BY playlist_genre;

SELECT * FROM genre_summary
ORDER BY avg_popularity DESC;

-- Create an artist summary view
CREATE OR REPLACE VIEW artist_summary AS
SELECT
    track_artist,
    COUNT(DISTINCT track_id) AS unique_tracks,
    COUNT(DISTINCT playlist_id) AS playlist_presence,
    ROUND(AVG(track_popularity), 2) AS avg_popularity,
    MAX(track_popularity) AS max_popularity,
    ROUND(AVG(danceability), 3) AS avg_danceability,
    ROUND(AVG(energy), 3) AS avg_energy
FROM cleaned_tracks
GROUP BY track_artist
HAVING COUNT(DISTINCT track_id) >= 5;

SHOW FULL TABLES WHERE Table_type = 'VIEW';