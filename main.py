import src.advanced_practice.duongdt_how_to_create_function as create_function


class Song:
    def __init__(self, name: str, playCount: int):
        self.name = name
        self.playCount = playCount

    def __str__(self):
        return self.name + " " + str(self.playCount)

def getMaxPlayCountSong(songList: typing.List[Song]) -> typing.Union[Song, None]:
    if len(songList) > 0:
        maxSong: Song = songList[0]
        for song in songList:
            if maxSong.playCount < song.playCount:
                maxSong = song
        return maxSong
    else:
        return None

def findSongByName(songs: typing.List[Song], conditionName: str) -> typing.List[Song]:
        foundSongList: typing.List[Song] = []
        for song in songs:
            indexFound = song.name.find(conditionName)
            if indexFound > -1:
                foundSongList.append(song)
        return foundSongList

def main():
    songs: typing.List[Song] = [
        Song(name= "Chung Ta Cua Hien Tai 1", playCount = 10000001),
        Song(name= "Chung Ta Cua Hien Tai 1", playCount = 10000001),
        Song(name= "Chung Ta Cua Hien Tai 2", playCount = 20000001),
        Song(name= "Chung Ta Cua Hien Tai 7", playCount = 70000001),
        Song(name= "Chung Ta Cua Hien Tai 4", playCount = 40000001),
        Song(name= "Chung Ta Cua Hien Tai 3", playCount = 30000001),
        Song(name= "Chung Ta Cua Hien Tai 5", playCount = 50000001),
        Song(name= "Chung Ta Cua Hien Tai 6", playCount = 60000001),
    ]

    foundSongList1 = findSongByName(songs= songs, conditionName= "Cua")
    # print(foundSongList1)
    print("foundSongList1 = ")
    for song in foundSongList1:
        print(song)
    
    songsFake: typing.List[int] = [1, 2 , 3 , 4 , 5]
    foundSongList = findSongByName(songs= songs, conditionName= "2")
    print("foundSongList = ")
    for song in foundSongList:
        print(song)
        
    song: Song = Song(name= "Chung Ta Cua Hien Tai 1", playCount = 10020001)


    textOfSong: str = str(song) #= song.__str__()
    print("textOfSong", textOfSong)

    maxSong = getMaxPlayCountSong(songList= songs)
    print("maxSong", maxSong)

main()
print("sai roi")
# thu nha

