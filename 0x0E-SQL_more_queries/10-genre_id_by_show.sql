-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- Use hbtn_0d_tvshows;
USE hbtn_0d_tvshows;

-- List all shows with linked genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
