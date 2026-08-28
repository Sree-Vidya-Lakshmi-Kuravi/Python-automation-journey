USE music_analysis_project;
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT track_id) AS unique_tracks
FROM raw_tracks;

-- Checking whether the track_id is NULL
SELECT COUNT(*) AS null_count FROM raw_tracks
WHERE track_id IS NULL; 

-- Checking the important columns
SELECT
    SUM(track_id IS NULL OR track_id = '') AS missing_track_id,
    SUM(track_name IS NULL OR track_name = '') AS missing_track_name,
    SUM(track_artist IS NULL OR track_artist = '') AS missing_track_artist,
    SUM(track_album_id IS NULL OR track_album_id = '') AS missing_track_album_id,
    SUM(playlist_id IS NULL OR playlist_id = '') AS missing_playlist_id,
    SUM(playlist_name IS NULL OR playlist_name = '') AS missing_playlist_name,
    SUM(playlist_genre IS NULL OR playlist_genre = '') AS missing_playlist_genre
FROM raw_tracks;

-- Check numeric columns for NULL
SELECT
    SUM(danceability IS NULL) AS null_danceability,
    SUM(energy IS NULL) AS null_energy,
    SUM(loudness IS NULL) AS null_loudness,
    SUM(speechiness IS NULL) AS null_speechiness,
    SUM(acousticness IS NULL) AS null_acousticness,
    SUM(instrumentalness IS NULL) AS null_instrumentalness,
    SUM(liveness IS NULL) AS null_liveness,
    SUM(valence IS NULL) AS null_valence,
    SUM(tempo IS NULL) AS null_tempo,
    SUM(duration_ms IS NULL) AS null_duration
FROM raw_tracks;

-- Check the range of popularity
SELECT
    MIN(track_popularity) AS min_pop,
    MAX(track_popularity) AS max_pop,
    AVG(track_popularity) AS avg_popularity
FROM raw_tracks;

-- Check audio-feature ranges
SELECT
    MIN(danceability) AS min_danceability,
    MAX(danceability) AS max_danceability,
    MIN(energy) AS min_energy,
    MAX(energy) AS max_energy,
    MIN(valence) AS min_valence,
    MAX(valence) AS max_valence
FROM raw_tracks;

-- Check the release-date formats
SELECT track_album_release_date, COUNT(*) AS occurrences FROM raw_tracks
GROUP BY track_album_release_date
ORDER BY occurrences DESC
LIMIT 20;

-- Check for missing release dates
SELECT
    SUM(track_album_release_date IS NULL
        OR TRIM(track_album_release_date) = '') AS missing_release_dates
FROM raw_tracks;

-- Check the genres
SELECT playlist_genre, COUNT(*) AS track_count
FROM raw_tracks
GROUP BY playlist_genre
ORDER BY track_count DESC;

-- Check the subgenres
SELECT playlist_subgenre, COUNT(*) AS track_count
FROM raw_tracks
GROUP BY playlist_subgenre
ORDER BY track_count DESC;

-- Check mode and key
SELECT
    MIN(`key`) AS min_key,
    MAX(`key`) AS max_key,
    MIN(mode) AS min_mode,
    MAX(mode) AS max_mode
FROM raw_tracks;

-- Check the remaining audio features
SELECT
    MIN(speechiness) AS min_speechiness,
    MAX(speechiness) AS max_speechiness,
    MIN(acousticness) AS min_acousticness,
    MAX(acousticness) AS max_acousticness,
    MIN(instrumentalness) AS min_instrumentalness,
    MAX(instrumentalness) AS max_instrumentalness,
    MIN(liveness) AS min_liveness,
    MAX(liveness) AS max_liveness,
    MIN(tempo) AS min_tempo,
    MAX(tempo) AS max_tempo,
    MIN(duration_ms) AS min_duration_ms,
    MAX(duration_ms) AS max_duration_ms
FROM raw_tracks;

