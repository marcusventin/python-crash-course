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


ok = make_album('OutKast', 'Speakerboxxx')
print(ok)

pn = make_album('paolo nutini', 'these streets', 10)
print(pn)