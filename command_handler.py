import os
from matplotlib import artist
from numpy import where

from soupsieve import select
from helper import yPrint, bPrint, rPrint, clear
from db_handler import DbHandler


class CommandHandler:
    def __init__(self):
        self.dbHandler = DbHandler()

    def getUserInput(self):
        print()
        yPrint("Choose a number from 1 to 7:")
        bPrint("1- Add new playlist")
        bPrint("2- Add song to a playlist")
        bPrint("3- get list of playlists")
        bPrint("4- get list of songs in a playlist")
        bPrint("5- Delete a playlist")
        bPrint("6- Delete a song from a playlist")
        bPrint("7- List songs by genre")
        bPrint("8- List songs by Artist")
        bPrint("0- Exit")
        print()

        try:
            userInput = int(input("Enter your choice:"))
        except:
            userInput = None

        if 1 >= userInput >= 10:
            print()
            rPrint("Error: invalid input!", True)
            rPrint("==================================", True)
            return None
        else:
            return userInput

    def createNewPlaylist(self):
        playlistName = input("Enter playlist name: ")
        genre = input("Enter playlist genre: ")
        self.dbHandler.db_addPlaylist(playlistName, genre)

    def getPlaylistNames(self):
        playlists = self.dbHandler.db_getPlaylists()
        print("Playlist names:")
        for playlist in playlists:
            print(playlist[1])

    def addSongToPlaylist(self, playlistName, songs):
        playlistId = self.dbHandler.db_getPlaylistIdByName(playlistName)
        if playlistId == None:
            print(f"Playlist {playlistName} does not exist!")
            return

        for song in songs:
            self.dbHandler.db_addSong(song["name"], song["genre"], song["description"],
                                      song["artist"], song["album"], False, playlistId)

            yPrint(f"song {song['name']} added to {playlistName}. ")

    # def getPlaylistSongs(playlistName):
    #     fileName = getPlaylistFileName(playlistName)
    #     isExist = os.path.exists(fileName)
    #     if isExist:
    #         with open(fileName, "r") as playlistFile:
    #             songNames = playlistFile.readlines()
    #         if len(songNames) == 0:
    #             print("Playlist is empty.")
    #         else:
    #             print(f"List of songs in {playlistName}:")
    #             for sName in songNames:
    #                 print(sName.strip())
    #     else:
    #         print(f"Playlist {playlistName} does not exist!")

    def getPlaylistSongs(self, playlistName):
        playlistId = self.dbHandler.db_getPlaylistIdByName(playlistName)
        if playlistId == None:
            print(f"Playlist {playlistName} does not exist!")
            return

        songs = self.dbHandler.db_getPlaylistSongs(playlistId)
        rPrint(f"List of songs in {playlistName}:", True)
        for song in songs:
            yPrint(song[1])

    def deletePlaylist(self, playlistName):
        playlistId = self.dbHandler.db_getPlaylistIdByName(playlistName)
        if playlistId == None:
            print(f"Playlist {playlistName} does not exist!")
            return

        self.dbHandler.db_deletePlayList(playlistId)
        print(f"Playlist {playlistName} deleted!")

    def deleteSong(self, playlistName, songName):
        playlistId = self.dbHandler.db_getPlaylistIdByName(playlistName)
        if playlistId == None:
            print(f"Playlist {playlistName} does not exist!")
            return

        self.dbHandler.db_deleteSongFromPlaylist(playlistId, songName)
        print(f"song {songName} is deleted from Playlist {playlistName}")

    def listSongsByGenre(self, genre):

        songs = self.dbHandler.db_listSongsByGenre(genre)
        if len(songs) == 0:
            print("No song found!")
        for song in songs:
            print(song[0])

    def listSongsByArtist(self, Artist):
        songs = self.dbHandler.db_listSongsByArtist(Artist)
        if len(songs) == 0:
            print("No song found!")
        for song in songs:
            print(song[0])

    def getSongInfo(self):
        songsInfo = []
        while True:
            songInfo = input(
                "Enter song name,genre,description,artist,album (':q' to stop): ")
            if songInfo != ":q":
                songInfoList = songInfo.split(",")
                while len(songInfoList) < 5:
                    songInfoList.append("")

                song = {"name": songInfoList[0], "genre": songInfoList[1],
                        "description": songInfoList[2], "artist": songInfoList[3], "album": songInfoList[4]}
                songsInfo.append(song)
            else:
                break

        return songsInfo

    def executeUserCommand(self, userInput):
        # execute selected command
        if userInput == 1:
            self.createNewPlaylist()
        elif userInput == 2:
            playlistName = input("Enter playlist name: ")
            songs = self.getSongInfo()
            self.addSongToPlaylist(playlistName, songs)
        elif userInput == 3:
            self.getPlaylistNames()
        elif userInput == 4:
            playlistName = input("Enter playlist name: ")
            self.getPlaylistSongs(playlistName)
        elif userInput == 5:
            playlistName = input("Enter playlist name: ")
            self.deletePlaylist(playlistName)
        elif userInput == 6:
            playlistName = input("Enter playlist name: ")
            songName = input("Enter song name: ")
            self.deleteSong(playlistName, songName)
        elif userInput == 7:
            genreName = input("Enter genre: ")
            self.listSongsByGenre(genreName)
        elif userInput == 8:
            artist = input("Enter Artist name : ")
            self.listSongsByArtist(artist)

        print("=================================")
        input("Press enter key to continue.")
        clear()
