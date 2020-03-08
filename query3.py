import musicbrainzngs

class MB_Query():
    def __init__(self, usersArtist, usersAlbum):
        # vars for holding what we'll need to use the MB lib
        self.artist = usersArtist
        self.album = usersAlbum
        self.MBResult = {}
        # borrowed authentication necessary for querying MB service
        self.agentAuth = musicbrainzngs.set_useragent(
            "python-musicbrainzngs-example",
            "0.1",
            "https://github.com/alastair/python-musicbrainzngs/",
        )

    def show_choices(self):
        # return the top 25 results from MB search using user input string
        choices = musicbrainzngs.search_artists(artist=self.artist)
        print(choices)
