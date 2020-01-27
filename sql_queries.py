# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

user_table_create = ("CREATE table IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar NOT NULL, last_name varchar NOT NULL, gender varchar, level varchar);")

song_table_create = ("CREATE table IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar NOT NULL, year int, duration int);")

artist_table_create = ("CREATE table IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude numeric, longitude numeric);")

time_table_create = ("CREATE table IF NOT EXISTS time (start_time date PRIMARY KEY, hour int NOT NULL, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL);")


songplay_table_create = ("CREATE table IF NOT EXISTS songplays (songplay_id int PRIMARY KEY, start_time bigint, \
                                                                user_id int , \
                                                                level varchar, song_id varchar, artist_id varchar, session_id int, \
                                                                location varchar, user_agent varchar);")

alter_songplay_fk_user_id = "alter table songplays add foreign key (user_id) REFERENCES users(user_id);"
alter_songplay_fk_song_id = "alter table songplays add foreign key (song_id) REFERENCES songs(song_id);"
alter_songplay_fk_artist_id = "alter table songplays add foreign key (artist_id) REFERENCES artists(artist_id);"

# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level)\
                        VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration)\
                          VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, longitude)\
                          VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")


time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
                          VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING")

# FIND SONGS

song_select = ("SELECT songs.song_id, songs.artist_id FROM songs JOIN artists ON\
                    songs.artist_id = artists.artist_id WHERE\
                    songs.title = %s AND\
                    artists.name = %s AND\
                    songs.duration = %s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
alter_table_queries = [alter_songplay_fk_artist_id, alter_songplay_fk_song_id, alter_songplay_fk_artist_id]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]