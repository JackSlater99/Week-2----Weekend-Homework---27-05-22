class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def react_favourite_song(self, playlist):
        if playlist[0] == self.fav_song:
            return "Whoo!"