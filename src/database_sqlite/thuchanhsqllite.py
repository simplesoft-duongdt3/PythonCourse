from os import name
import sqlite3
import math
import typing
conn=sqlite3.connect('chinook.db')
cursor=conn.execute("SELECT * FROM genres LIMIT 10")
result=cursor.fetchall()
print('\n','Get rows by fetch one',result)


cursor4=conn.execute("SELECT  COUNT (*) FROM albums  ")

result4=cursor4.fetchall()
print("\n","So luong album =",result4,result4[0])

totalalbum=result4[0]
print(totalalbum)


class Albums:
    def __init__(self,id:int,title:str,artisid:int):
        self.id=id
        self.title=title
        self.artisid=artisid

    def __str__(self) -> str:
        return str(self.id) + " " +str(self.title)+" "+str(self.artisid)


def GetAlbumatPage(sotrang:int)->typing.List[Albums]:
    conn=sqlite3.connect('chinook.db')
    offset:int=(sotrang-1)*10
    cursor5=conn.execute(str.format("SELECT  * FROM albums LIMIT 10 offset {offset} ",offset=offset))
    result5=cursor5.fetchall()
    list1:typing.List[Albums]=[]
    for newAlbum in result5:
        album:Albums= Albums(id=newAlbum[0],title=newAlbum[1],artisid=newAlbum[2])
        list1.append(album)

    return list1

baihattim=GetAlbumatPage(sotrang=2)
for album in baihattim:
    print(album)


class Track:
    def __init__(self,trac:int,name:str,albumld:int):
        self.trac=trac
        self.name=name
        self.albumld=albumld

    def __str__(self) -> str:
            return str(self.trac) + " " +str(self.name)+" "+str(self.albumld)


def GetTrackListinAlbum(albumid:int) -> typing.List[Track]:
    conn=sqlite3.connect('chinook.db')
    cursor=conn.execute(str.format("""SELECT trackid,name,albumid FROM tracks AS tr WHERE albumid ={albumid}""",albumid=albumid))
    result=cursor.fetchall()
    listtrack:typing.List[Track]=[]
    for trackdb in result:
        track:Track= Track(trac=trackdb[0],name=trackdb[1],albumld=trackdb[2])
        listtrack.append(track)

    return listtrack  

baihats = GetTrackListinAlbum(1)
print('cac bai hat la')
for track in baihats:
    print(track)

class Artist:
    def __init__(self,albumid:int,name:str,artistid:int):
        self.albumid=albumid
        self.name=name
        self.artisid=artistid

    def __str__(self) -> str:
            return str(self.albumid) + " " +str(self.name)+" "+str(self.artisid)



def GetTrackList(albumid:int)->typing.Optional[Artist]:
    conn=sqlite3.connect('chinook.db')
    cursor=conn.execute(str.format("""SELECT ab.albumid,ar.name,ar.artistid
From albums AS ab
INNER JOIN artists AS ar
ON ab.artistid=ar.ArtistId
WHERE ab.albumid ={albumid}""",albumid=albumid))
    artistuple:typing.Tuple=cursor.fetchone()
    
    artisid=Artist(albumid=artistuple[0],name=artistuple[1],artistid=artistuple[2])

    return artisid


a=GetTrackList(albumid=1)
print(a)


