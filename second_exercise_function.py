def make_album(artist, album_title, number_songs= None):
    info = {'Artist_Name' : artist, 'Album_Title' : album_title}
    if number_songs:
        info['Songs'] = number_songs
    return info
while True:
    print("Please give required info")
    print("Press q any time to quit")
    artist = input("Enter Your Favourite Artist name: ")
    if artist == 'q':
        break
    album = input("Enter title of favourite album: ")
    if album == 'q':
        break
    songs = input("How many songs in that album: ")
    if songs == 'q':
        break
    User_given = make_album(artist, album, songs)
    print(User_given)