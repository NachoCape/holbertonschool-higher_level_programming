-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
SELECT tt.title, tg.genre_id FROM tv_shows tt LEFT JOIN tv_show_genres tg ON tt.id=tg.show_id WHERE tg.genre_id IS NULL ORDER BY tt.title, tg.genre_id ASC;