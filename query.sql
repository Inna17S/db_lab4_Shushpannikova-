-- Select * from Artists;
-- Select * from Genre;
-- Select * from Songs;
-- Select * from Chart;
-- Select * from SongsGenre;

--1 запит - кількість треків у кожному жанрі
SELECT Genre.genre_name, COUNT(Genre) AS track_count
FROM SongsGenre
JOIN Genre ON SongsGenre.GenreID = Genre.GenreID
GROUP BY Genre.genre_name;


--2 запит - Вивести таблицю енергійності треку та його позицію в чарті
SELECT Chart.position, Songs.energy
FROM Chart
JOIN Songs ON Chart.Song_ID = Songs.Song_ID;


--3 запит - Вивести таблицю тривалості треку та його позицію в чарті
SELECT Chart.position, Songs.duration_ms
FROM Chart
JOIN Songs ON Chart.Song_ID = Songs.Song_ID;
