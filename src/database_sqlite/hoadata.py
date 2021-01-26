import sqlite3
import math
import typing

conn=sqlite3.connect('chinook.db')
cursor3=conn.execute('select * from genres limit 3')
result3=cursor3.fetchone()
print('\n', 'get rows by fetch one', type(result3), result3)

cursor2=conn.execute('select * from genres limit 3')
result2=cursor2.fetchall()
print('\n', 'get rows by fetch all', type(result2), result2)

print('\n', 'get rows by iterable')
cursor1=conn.execute('select * from genres limit 3')
for row in cursor1:
    print('row = ', row[0], row[1])


cursor0=conn.execute('select count (*) from albums')
result0=cursor0.fetchone()
total =result0[0]
print('\n', 'total of albums',  total)

cursor10=conn.execute('select count (*) from albums')
result10=cursor10.fetchall()
totalPages= math.ceil(total/10)
print('\n', 'total of pages',  totalPages)

class Album :
    def __init__(self,id: int, title:str, arit: str):
        self.id=id
        self.title=title
        self.arit=arit 

    def __str__(self) -> str:
        return str(self.id) +" " + str(self.title) + " " + str(self.arit)


def GetAlbumAtPage ( page:int ) -> typing.List[Album]: 
    conn=sqlite3.connect('chinook.db')
    offset=(page-1)*10
    cursor11=conn.execute(str.format('select * from albums limit 10 offset {offset}', offset=offset))
    ##cursor11=conn.execute('select * from albums limit 10 offset '+ str(offset))
    result11=cursor11.fetchall()
    list1 : typing.List[Album] = []
    for albumTuple in result11:
        album: Album = Album(id=albumTuple[0],title=albumTuple[1],arit=albumTuple[2])
        list1.append(album)
    return list1
a= GetAlbumAtPage(page=4)
for album in a :
    print(album)




        


