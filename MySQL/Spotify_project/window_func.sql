-- Top 10 artists by average popularity
SELECT
    track_artist,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
GROUP BY track_artist
HAVING COUNT(DISTINCT track_id) >= 5
ORDER BY avg_popularity DESC
LIMIT 10;

-- Top 5 tracks within each genre
WITH ranked_tracks AS (
    SELECT playlist_genre, track_id, track_name, track_artist, track_popularity,
        DENSE_RANK() OVER (
            PARTITION BY playlist_genre
            ORDER BY track_popularity DESC
        ) AS genre_rank
    FROM cleaned_tracks)
SELECT playlist_genre, track_name, track_artist, track_popularity, genre_rank
FROM ranked_tracks
WHERE genre_rank <= 5
ORDER BY playlist_genre, genre_rank;

-- Genre performance compared with overall popularity
WITH genre_stats AS (
    SELECT
        playlist_genre,
        ROUND(AVG(track_popularity), 2) AS avg_genre_popularity
    FROM cleaned_tracks
    GROUP BY playlist_genre),
overall_stats AS (
    SELECT
        ROUND(AVG(track_popularity), 2) AS overall_popularity
    FROM cleaned_tracks)
SELECT
    g.playlist_genre,
    g.avg_genre_popularity,
    o.overall_popularity,
    ROUND(g.avg_genre_popularity - o.overall_popularity, 2) AS difference_from_overall
FROM genre_stats g
CROSS JOIN overall_stats o
ORDER BY difference_from_overall DESC;

-- Popularity rank of every track within its genre
WITH track_ranking AS (
    SELECT playlist_genre, track_name, track_artist,track_popularity,
        RANK() OVER (
            PARTITION BY playlist_genre
            ORDER BY track_popularity DESC
) AS popularity_rank
    FROM cleaned_tracks)
SELECT * FROM track_ranking
WHERE popularity_rank <= 10
ORDER BY playlist_genre, popularity_rank;

-- Compare each track's popularity with its genre average
SELECT DISTINCT track_id, track_name, track_artist, playlist_genre, track_popularity,
    ROUND(
        AVG(track_popularity) OVER (
            PARTITION BY playlist_genre), 2
    ) AS genre_avg_popularity,
    ROUND(track_popularity - AVG(track_popularity) OVER (
            PARTITION BY playlist_genre), 2
    ) AS difference_from_genre_avg
FROM cleaned_tracks
ORDER BY difference_from_genre_avg DESC
LIMIT 20;

-- Most frequently appearing tracks
SELECT track_id, track_name, track_artist,
    COUNT(DISTINCT playlist_id) AS playlist_count
FROM cleaned_tracks
GROUP BY track_id, track_name, track_artist
ORDER BY playlist_count DESC
LIMIT 20;

-- Artists with the widest playlist presence
SELECT
    track_artist,
    COUNT(DISTINCT playlist_id) AS playlist_count,
    COUNT(DISTINCT track_id) AS unique_tracks
FROM cleaned_tracks
GROUP BY track_artist
ORDER BY playlist_count DESC
LIMIT 20;

-- Does danceability correlate with popularity?
SELECT
    CASE
        WHEN danceability < 0.25 THEN 'Very Low'
        WHEN danceability < 0.50 THEN 'Low'
        WHEN danceability < 0.75 THEN 'High'
        ELSE 'Very High'
    END AS danceability_level,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
GROUP BY danceability_level
ORDER BY avg_popularity DESC;

-- Yearly popularity trend
SELECT release_year,
    COUNT(DISTINCT track_id) AS unique_tracks,
    ROUND(AVG(track_popularity), 2) AS avg_popularity
FROM cleaned_tracks
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year;