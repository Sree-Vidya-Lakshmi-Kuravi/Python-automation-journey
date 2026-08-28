CREATE TABLE cleaned_tracks AS
SELECT *
FROM raw_tracks
WHERE track_id IS NOT NULL
  AND TRIM(track_id) <> ''
  AND track_name IS NOT NULL
  AND TRIM(track_name) <> ''
  AND track_artist IS NOT NULL
  AND TRIM(track_artist) <> ''
  AND playlist_id IS NOT NULL
  AND TRIM(playlist_id) <> '';

SELECT COUNT(*) AS cleaned_rows
FROM cleaned_tracks;

-- Compare raw vs cleaned
SELECT
    (SELECT COUNT(*) FROM raw_tracks) AS raw_rows,
    (SELECT COUNT(*) FROM cleaned_tracks) AS cleaned_rows;

DESCRIBE cleaned_tracks;
ALTER TABLE cleaned_tracks
ADD COLUMN release_year INT;
UPDATE cleaned_tracks
SET release_year = CAST(LEFT(track_album_release_date, 4) AS UNSIGNED)
WHERE track_album_release_date IS NOT NULL
  AND TRIM(track_album_release_date) <> '';
-- CAST(... AS UNSIGNED): converts that text into a number.

SELECT
    track_album_release_date,
    release_year
FROM cleaned_tracks
LIMIT 20;

-- Check for invalid years
SELECT
    MIN(release_year) AS min_year,
    MAX(release_year) AS max_year
FROM cleaned_tracks
WHERE release_year IS NOT NULL;

SELECT
    release_year,
    COUNT(*) AS track_count
FROM cleaned_tracks
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year DESC
LIMIT 20;

-- Validate the 0–1 audio features
SELECT
    SUM(danceability < 0 OR danceability > 1) AS invalid_danceability,
    SUM(energy < 0 OR energy > 1) AS invalid_energy,
    SUM(speechiness < 0 OR speechiness > 1) AS invalid_speechiness,
    SUM(acousticness < 0 OR acousticness > 1) AS invalid_acousticness,
    SUM(instrumentalness < 0 OR instrumentalness > 1) AS invalid_instrumentalness,
    SUM(liveness < 0 OR liveness > 1) AS invalid_liveness,
    SUM(valence < 0 OR valence > 1) AS invalid_valence
FROM cleaned_tracks;

-- Validate popularity
SELECT
    SUM(track_popularity < 0 OR track_popularity > 100) AS invalid_popularity,
    MIN(track_popularity) AS min_popularity,
    MAX(track_popularity) AS max_popularity
FROM cleaned_tracks;

-- Validate key and mode
SELECT
    SUM(`key` < 0 OR `key` > 11) AS invalid_key,
    SUM(mode NOT IN (0, 1)) AS invalid_mode,
    MIN(`key`) AS min_key,
    MAX(`key`) AS max_key
FROM cleaned_tracks;

-- Check tempo
SELECT
    MIN(tempo) AS min_tempo,
    MAX(tempo) AS max_tempo,
    AVG(tempo) AS avg_tempo
FROM cleaned_tracks;

SELECT COUNT(*) AS invalid_tempo
FROM cleaned_tracks
WHERE tempo <= 0;

-- Check duration
ALTER TABLE cleaned_tracks
ADD COLUMN duration_minutes DECIMAL(6,2);
UPDATE cleaned_tracks
SET duration_minutes = ROUND(duration_ms / 60000, 2)
WHERE duration_ms IS NOT NULL;

-- Validate duration
SELECT
    MIN(duration_ms) AS min_duration_ms,
    MAX(duration_ms) AS max_duration_ms,
    MIN(duration_minutes) AS min_duration_minutes,
    MAX(duration_minutes) AS max_duration_minutes
FROM cleaned_tracks;

SELECT COUNT(*) AS invalid_duration
FROM cleaned_tracks
WHERE duration_ms <= 0;

-- Check release_year
SELECT
    MIN(release_year) AS min_release_year,
    MAX(release_year) AS max_release_year
FROM cleaned_tracks
WHERE release_year IS NOT NULL;

SELECT COUNT(*) AS invalid_release_year
FROM cleaned_tracks
WHERE release_year IS NOT NULL
  AND (release_year < 1900 OR release_year > YEAR(CURDATE()));

DESCRIBE cleaned_tracks;

-- Check the row count one more time
SELECT COUNT(*) AS total_cleaned_rows
FROM cleaned_tracks;

-- Check whether our newly created columns contain NULLs
SELECT
    SUM(release_year IS NULL) AS missing_release_year,
    SUM(duration_minutes IS NULL) AS missing_duration_minutes
FROM cleaned_tracks;

-- Check the cleaned data sample
SELECT
    track_id,
    track_name,
    track_artist,
    track_popularity,
    playlist_genre,
    playlist_subgenre,
    danceability,
    energy,
    valence,
    tempo,
    duration_ms,
    duration_minutes,
    track_album_release_date,
    release_year
FROM cleaned_tracks
LIMIT 10;

-- Trim extra spaces
SELECT COUNT(*) AS track_names_with_spaces
FROM cleaned_tracks
WHERE track_name <> TRIM(track_name);

SELECT COUNT(*) AS artist_names_with_spaces
FROM cleaned_tracks
WHERE track_artist <> TRIM(track_artist);

SELECT COUNT(*) AS playlist_names_with_spaces
FROM cleaned_tracks
WHERE playlist_name <> TRIM(playlist_name);

-- Check inconsistent capitalization in genres
SELECT
    playlist_genre,
    COUNT(*) AS count
FROM cleaned_tracks
GROUP BY playlist_genre
ORDER BY playlist_genre;
SELECT
    playlist_subgenre,
    COUNT(*) AS count
FROM cleaned_tracks
GROUP BY playlist_subgenre
ORDER BY playlist_subgenre;

-- Create popularity_category
ALTER TABLE cleaned_tracks
ADD COLUMN popularity_category VARCHAR(20);

UPDATE cleaned_tracks
SET popularity_category =
    CASE
        WHEN track_popularity < 25 THEN 'Low'
        WHEN track_popularity < 50 THEN 'Moderate'
        WHEN track_popularity < 75 THEN 'High'
        ELSE 'Very High'
    END;

-- Create energy_level
ALTER TABLE cleaned_tracks
ADD COLUMN energy_level VARCHAR(20);
UPDATE cleaned_tracks
SET energy_level =
    CASE
        WHEN energy < 0.40 THEN 'Low'
        WHEN energy < 0.70 THEN 'Medium'
        ELSE 'High'
    END;

-- Create duration_category
ALTER TABLE cleaned_tracks
ADD COLUMN duration_category VARCHAR(20);

UPDATE cleaned_tracks
SET duration_category =
    CASE
        WHEN duration_minutes < 3 THEN 'Short'
        WHEN duration_minutes <= 5 THEN 'Medium'
        ELSE 'Long'
    END;

SELECT
    track_name,
    track_popularity,
    popularity_category,
    energy,
    energy_level,
    duration_minutes,
    duration_category
FROM cleaned_tracks
LIMIT 20;

SELECT
    popularity_category,
    COUNT(*) AS track_count
FROM cleaned_tracks
GROUP BY popularity_category
ORDER BY track_count DESC;

SELECT
    energy_level,
    COUNT(*) AS track_count
FROM cleaned_tracks
GROUP BY energy_level
ORDER BY track_count DESC;

SELECT
    duration_category,
    COUNT(*) AS track_count
FROM cleaned_tracks
GROUP BY duration_category
ORDER BY track_count DESC;