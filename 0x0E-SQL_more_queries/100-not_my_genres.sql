-- List genres not linked to Detxter
SELECT DISTINCT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NULL 
OR tv_genres.id NOT IN (
	SELECT tv_genres.id 
	FROM tv_show_genres 
	JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id 
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id 
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;

