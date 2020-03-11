import musicbrainzngs


class mbQuery:
    def __init__(self, users_artist):
        # vars to utilize library functionality
        self.artist = users_artist
        # self.album = usersAlbum
        self.artist_mbid = ''
        self.selected_album_mbid = ''
        self.MB_queryResult = {}
        # borrowed authentication necessary for querying MB service
        self.agentAuth = musicbrainzngs.set_useragent(
            "python-musicbrainzngs-example",
            "0.1",
            "https://github.com/alastair/python-musicbrainzngs/",
        )

    def with_input_browse_recordings(self):
        # return the top 25 results from MB search using user input string
        tmp = musicbrainzngs.search_artists(self.artist)
        self.artist_mbid = tmp['artist-list'][0]['id']
        self.MB_queryResult = musicbrainzngs.browse_releases(artist=self.artist_mbid)

    def show_tracks(self):
        # self.MB_trackResult = musicbrainzngs.browse_recordings(self.MB_releaseID)
        print('hello')
