import musicbrainzngs

class MB_Query():
    def __init__(self, usersArtist, usersAlbum):
        # vars for holding what we'll need to use the MB lib
        self.artist = usersArtist
        self.album = usersAlbum
        self.MB_albumResult = {}
        self.MB_artistResult = {}
        # borrowed authentication necessary for querying MB service
        self.agentAuth = musicbrainzngs.set_useragent(
            "python-musicbrainzngs-example",
            "0.1",
            "https://github.com/alastair/python-musicbrainzngs/",
        )

    def show_choices(self):
        # return the top 25 results from MB search using user input string
        # artist_choices = musicbrainzngs.search_artists(artist=self.artist)
        # self.MB_a = musicbrainzngs.
        # self.MBResult = musicbrainzngs.search_releases(self.album)
        # hafta get the artist id first
        self.MB_artistResult = musicbrainzngs.search_artists(artist=self.artist)
        queryID = self.MB_artistResult['artist-list'][0]
        tmp = queryID['id']
        # print(artist_choices)
        # print(self.MBResult)
        recordRTN = musicbrainzngs.browse_recordings(artist=tmp)
        print(recordRTN)
