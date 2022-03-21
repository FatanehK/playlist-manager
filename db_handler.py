
from unicodedata import name
import psycopg2


class DbHandler:
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname=PlaylistManager user=postgres password=12345678"
        )

    def db_getPlaylists(self):
        # Connect to your postgres DB

        # Open a cursor to perform database operations
        with self.conn.cursor() as cur:
            # Execute a query
            cur.execute("SELECT * FROM playlists")

            # Retrieve query results
            playlists = cur.fetchall()

        return playlists

    def db_addPlaylist(self, playlistName, genre):
        # Connect to your postgres DB

        # Open a cursor to perform database operations
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO public.playlists VALUES (DEFAULT,%s,%s)",
                (playlistName, genre)
            )
            self.conn.commit()

    def db_getPlaylistIdByName(self, playlistName):
        # Connect to your postgres DB

        # Open a cursor to perform database operations
        with self.conn.cursor() as cur:
            cur.execute(
                f"SELECT id FROM playlists WHERE name LIKE '{playlistName}'")
            record = cur.fetchone()
            if record == None:
                return None
            else:
                return record[0]

    def db_addSong(self, name, genre, description, artist, album, favorite, playlistId):

        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO public.songs VALUES (DEFAULT,%s,%s,%s,%s,%s,%s,%s)",
                        (name, genre, description, artist, album, favorite, playlistId))
            self.conn.commit()

    def db_getPlaylistSongs(self, playlistId):

        # Open a cursor to perform database operations
        with self.conn.cursor() as cur:
            cur.execute(
                f"select * from songs where playlist_id = {playlistId}")
            songs = cur.fetchall()

            return songs

    def db_deletePlayList(self, id):
        with self.conn.cursor()as cur:
            cur.execute(f"delete from playlists where id ={id} ")
            cur.execute(f"delete from songs where playlist_id ={id} ")
            self.conn.commit()

    def db_deleteSongFromPlaylist(self, playlistId, songName):
        with self.conn.cursor()as cur:
            cur.execute(
                f"delete from songs where playlist_id={playlistId} and name like '{songName}' ")
            self.conn.commit()

    def db_listSongsByGenre(self, genre):
        with self.conn.cursor() as cur:
            cur.execute(
                f"select name from songs where genre like '{genre}'")

            songs = cur.fetchall()
            return songs

    def db_listSongsByArtist(self, Artist):
        with self.conn.cursor() as cur:
            cur.execute(f"select name from songs where Artist like '{Artist}'")

            songs = cur.fetchall()
            return songs
