def make_album(artist, album, no_songs=None):
    if no_songs:
        album = {
            'artist' : artist.title(),
            'album' : album.title(),
            'no_songs' : no_songs,
            }
    else:
        album = {
            'artist' : artist.title(),
            'album' : album.title(),
            }
    return(album)

while True:
    artist = input("\nEnter 'q' to quit.\nOtherwise enter artist name: ")
    if artist == "q":
        break
    else:
        album = input("Enter album name: ")
        if album == "q":
            break
    print(make_album(artist, album))