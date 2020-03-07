# this function takes the musicbrainz query and creates region labels consistent
# with audacity standards ie utf-8 ascii tab delim text file to

import sys
import musicbrainzngs
import urllib

# create the menu interaction for user input
# audacity scripting pipeline interaction
class mbQuery:
    def __init__(self, artist, album):
        self.uEntryArtist = artist
        self.uEntryAlbum = album
        self.queryID = ''
        self.artistReturns = {}

        # borrowed authentication necessary for querying MB service
        self.agentAuth = musicbrainzngs.set_useragent(
            "python-musicbrainzngs-example",
            "0.1",
            "https://github.com/alastair/python-musicbrainzngs/",
        )
        # query MB db using hardcoded values and get MB artist id

    def initMBQuery(self, artist, album ):
        artistsReturns = musicbrainzngs.search_artists(artist=self.uEntryArtist)

        # print all the results
        # for artist in theReturns['artist-list']:
        #     print(u"{id}: {name}".format(id=artist['id'], name=artist["name"]))

        # get the MBID_artist
        # here using hardcoded top result regardless of correctness

        queryID = artistsReturns['artist-list'][0]

        # this is the returned top MDIB_artist
        tmp = queryID['id']
    # #########################################################################
    # TODO: release id is hardcoded
    # take track length dictionary and use to create audacity label track txt file

    #########################################################################

    # get a dictionary of all the recordings using artistid
    # browserecordings returns recordigns linked to an artist or relase with MB artist or release id?
    recordRTN = musicbrainzngs.browse_recordings(release='d7cb737c-1583-41ba-98c2-356e4531e932')
    # otherReturns = musicbrainzngs.browse_recordings(tmp)
    print(recordRTN)
    # display all discrete recorded songs

    # create the dictionary to hold the track lengths and track titles
    trackLengthList = []
    trackTitleList = []
    for track in recordRTN['recording-list']:
        trackLengthList.append(track['length'])
        trackTitleList.append(track['title'])

    print(trackLengthList)


    # for record in otherReturns['recording-list']:
    #     print(u"{id}: {title}".format(id=record['id'], title=record['title']))

    # get a dictionary of release groups ie albums using MB artistid
    # can filter here wiwth musicbrainz.VALID_RELEASE_TYPES
    ##releaseGroupReturns = musicbrainzngs.browse_release_groups(tmp)

    # display release group? MBID  and titiel for <25 all the group releases
    # for record in releaseGroupReturns['release-group-list']:
    #     print(u"{id}: {title}".format(id=record['id'], title=record['title']))
    #
    # hrdCoRelGrpID = '510a9054-d64f-3e82-a901-dd95af76fc59'

    # hardcoded release-group-list MBID
    # albumInfo = musicbrainzngs.get_release_group_by_id(hrdCoRelGrpID)

    # display the album info using release-group MBID

    # print(albumInfo)

    # albumInfo2 = musicbrainzngs.get_release_by_id()
    # result = musicbrainzngs.get_artist_by_id(tmp,
    #               includes=["release-groups"], release_type=["album"])
    # for release_group in result["artist"]["release-group-list"]:
    #     print("{title} ({type})".format(title=release_group["title"],
    #                                     type=release_group["type"]))


    # albumID = '7d24c33c-dbf0-4951-a71d-fcda5e0aad24'
    # albumID ='47402901-7f0d-4762-8d36-d83c062e6ffd'
    # albumID = 'd7cb737c-1583-41ba-98c2-356e4531e932'

    # userReleaseID = '510a9054-d64f-3e82-a901-dd95af76fc59'
    # tracks = musicbrainzngs.get_release_by_id(tmp)

    # theAlbum = musicbrainzngs.search_releases(uEntryAlbum)

    # print(theAlbum)
    # print(tracks)
    # theAlbum2 = musicbrainzngs.search_release_groups(userReleaseID)

    # print(theAlbum2)

    # track = musicbrainzngs
    # print(track)

    # result = musicbrainzngs.get_releases_by_discid(disc.id, includes=["artists", "recordings"])

    # vars for track length summation (running total)
    # track length is in milliseconds
    trackTmp = 0.0

    # string for the output line
    # tmpLine = ''

    # open file for writing
    f = open("labels_test.txt", "w")

    # iterate through both lists
    for i, j in zip(trackLengthList, trackTitleList):
        trackLen = float(i)
        trackNam = j
        trackRegStart = trackTmp
        trackRegEnd = trackRegStart + trackLen
        trackTmp = trackRegEnd
        # converting to seconds here
        tmpLine = f'{trackRegStart/1000}\t{trackRegEnd/1000}\t{j}\n'
        # write line to file
        f.write(tmpLine)

    # close the txt file
    f.close()

