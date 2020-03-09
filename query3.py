import musicbrainzngs

class MB_Query():
    def __init__(self, usersArtist, usersAlbum):
        # vars for holding what we'll need to use the MB lib
        self.artist = usersArtist
        self.album = usersAlbum
        self.MB_albumResult = {}
        self.MB_artistResult = {}
        self.MB_queryResult = {}
        self.MB_artistID = ''
        self.MB_releaseID = ''
        # borrowed authentication necessary for querying MB service
        self.agentAuth = musicbrainzngs.set_useragent(
            "python-musicbrainzngs-example",
            "0.1",
            "https://github.com/alastair/python-musicbrainzngs/",
        )

        self.MB_obj = {}

    def show_choices(self):
        # return the top 25 results from MB search using user input string
        # artist_choices = musicbrainzngs.search_artists(artist=self.artist)
        # self.MB_a = musicbrainzngs.
        # self.MBResult = musicbrainzngs.search_releases(self.album)

        # # hafta get the artist id first
        # self.MB_artistResult = musicbrainzngs.search_artists(artist=self.artist)

        self.MB_queryResult = musicbrainzngs.search_release_groups(artist=self.artist, release=self.album)

        # print(self.MB_queryResult)

        # queryID = self.MB_artistResult['artist-list'][0]
        # self.MB_artistID = queryID['id']
        #
        # self.MB_albumResult = musicbrainzngs.browse_recordings(artist=self.MB_artistID)
        # print(self.MB_albumResult)

