-- c
-- c
SELECT tv_genres.name AS name FROM tv_show_genres JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.show_id = 8 ORDER BY name ASC;