from random import randint

#CLASSES

class Playlist():
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon
        self.songs = []

    def view(self):
        if len(self.songs) == 1:
            return f"{self.icon} {self.name} ({len(self.songs)} song)"
        else:
            return f"{self.icon} {self.name} ({len(self.songs)} songs)"

class Song():
    def __init__(self, title, artist, duration, playlist):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.id = randint(100000, 999999)
        self.playlist = playlist

    def view(self):
        return f"🔹 {self.title} - By {self.artist} [{self.duration}] (ID: {self.id})"

#FUNCTIONS

playlists = []
def create_playlist():
    print("\nCreating a new playlist...")
    name = input("\nEnter playlist's name:\n")
    print("\nSelect an icon for your playlist:")
    choosing = True
    while choosing:
        print("""1 - 🎵   2 - 🎶   3 - 🎧
4 - 📻   5 - 🎤   6 - 🎸
7 - 🎹   8 - 🥁   9 - 🪩""")
        select_icon = input()
        if select_icon == "1":
            icon = "🎵"
            choosing = False
        elif select_icon == "2":
            icon = "🎶"
            choosing = False
        elif select_icon == "3":
            icon = "🎧"
            choosing = False
        elif select_icon == "4":
            icon = "📻"
            choosing = False
        elif select_icon == "5":
            icon = "🎤"
            choosing = False
        elif select_icon == "6":
            icon = "🎸"
            choosing = False
        elif select_icon == "7":
            icon = "🎹"
            choosing = False
        elif select_icon == "8":
            icon = "🥁"
            choosing = False
        elif select_icon == "9":
            icon = "🪩"
            choosing = False
        else:
            print("\nInvalid option! Please select another icon:")
    playlist = Playlist(name, icon)
    playlists.append(playlist)
    print("\nPlaylist succesfully created!")
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

songs = []
def create_song():
    if len(playlists) == 0:
        print("\nYou haven't created any playlists yet!")
    else:
        print("\nAdding a new song...")
        title = input("\nEnter song's title:\n")
        artist = input("\nEnter song's artist:\n")
        duration = input("\nEnter song's duration:\n")
        print("\nTo which playlist do you want to add it?")
        choosing = True
        while choosing:
            for i in range(len(playlists)):
                print(f"  {i + 1} - {playlists[i].view()}")
            playlist = input()
            if playlist.isdigit():
                for i in playlists:
                    if str(playlists.index(i)) == str(int(playlist) - 1):
                        song = Song(title, artist, duration, i)
                        songs.append(song)
                        i.songs.append(song)
                        print(f"\nSong succesfully added to {i.name}!")
                        choosing = False
                        break
            if choosing:
                print("\nInvalid option! Please select another playlist:")
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

def view_playlists():
    if len(playlists) == 0:
        print("\nYou haven't created any playlists yet!")
    else:
        print("\nYour playlists:")
        for i in range(len(playlists)):
            print("  ",playlists[i].view())
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

def view_songs():
    if len(playlists) == 0:
        print("\nYou haven't created any playlists yet!")
    elif len(songs) == 0:
        print("\nYou haven't added any songs yet!")
    else:
        print("\nSelect a playlist to open:")
        choosing = True
        while choosing:
            for i in range(len(playlists)):
                print(f"  {i + 1} - {playlists[i].view()}")
            playlist = input()
            if playlist.isdigit():
                for i in playlists:
                    if str(playlists.index(i)) == str(int(playlist) - 1):
                        print(f"\n{i.view()}")
                        for e in i.songs:
                            print(f"  {e.view()}")
                        choosing = False
                        break
            if choosing:
                print("\nInvalid option! Please select another playlist:")
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

def delete_playlist():
    if len(playlists) == 0:
        print("\nYou haven't created any playlists yet!")
    else:
        print("\nSelect a playlist to delete:")
        choosing = True
        while choosing:
            for i in range(len(playlists)):
                print(f"  {i + 1} - {playlists[i].view()}")
            playlist = input()
            if playlist.isdigit():
                for i in playlists:
                    if str(playlists.index(i)) == str(int(playlist) - 1):
                        playlists.remove(i)
                        print(f"\n{i.name} playlist succesfully deleted!")
                        choosing = False
                        break
            if choosing:
                print("\nInvalid option! Please select another playlist:")
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

def delete_song():
    if len(playlists) == 0:
        print("\nYou haven't created any playlists yet!")
    elif len(songs) == 0:
        print("\nYou haven't added any songs yet!")
    else:
        print("\nSelect a playlist to remove a song from:")
        choosing = True
        while choosing:
            for i in range(len(playlists)):
                print(f"  {i + 1} - {playlists[i].view()}")
            playlist = input()
            if playlist.isdigit():
                for i in playlists:
                    if str(playlists.index(i)) == str(int(playlist) - 1):
                        print(f"\n{i.view()}")
                        print(f"Select a song to remove from {i.name}")
                        while choosing:
                            for e in i.songs:
                                print(f"  {i.songs.index(e) + 1} - {e.view()}")
                            song = input()
                            if song.isdigit():
                                for e in i.songs:
                                    if str(i.songs.index(e)) == str(int(song) - 1):
                                        i.songs.remove(e)
                                        songs.remove(e)
                                        print(f"\n{e.title} song succesfully deleted!")
                                        choosing = False
                                        break
                            if choosing:
                                print("\nInvalid option! Please select another song:")
                        choosing = False
                        break
            if choosing:
                print("\nInvalid option! Please select another playlist:")
    input("\n\033[3mPress [ENTER] to return to the main menu...\033[0m")

#MENU

run = True
while run:
    print("""
=========================================
        MUSIC TRACKER & ORGANIZER™
=========================================
1 - Create a new playlist
2 - Add a song to a playlist
3 - View all my playlists
4 - View songs from a playlist
5 - Delete a playlist
6 - Remove a song from a playlist
0 - Exit""")
    option = input()

    if option == "1":
        create_playlist()
    elif option == "2":
        create_song()
    elif option == "3":
        view_playlists()
    elif option == "4":
        view_songs()
    elif option == "5":
        delete_playlist()
    elif option == "6":
        delete_song()
    elif option == "0":
        run = False

print("\nThanks for using MUSIC TRACKER & ORGANIZER™!\n")