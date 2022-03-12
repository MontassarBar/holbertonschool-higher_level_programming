-- c
-- c
SELECT tv_shows.title AS title FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.genre_id = 5 ORDER BY title ASC;