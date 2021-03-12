import sqlite3
import math
import typing
conn=sqlite3.connect('chinook.db')

cursor3=conn.execute("SELECT * FROM genres LIMIT 3")
result3=cursor3.fetchone()
print("\n","Get rows by fetch one ",type(result3),result3)

cursor2=conn.execute("SELECT * FROM genres LIMIT 10")
result2=cursor2.fetchall()
print("\n","Get rows by fetch all",type(result2),result2)

print("\n","Get rows by Iterable")
cursor1=conn.execute("SELECT * FROM genres LIMIT 3")
for row in cursor1:
    print("row=",row[0],row[1])



cursor4=conn.execute("SELECT  COUNT (*) FROM albums  ")

result4=cursor4.fetchone()
print("\n","So luong album =",result4,result4[0])

totalalbum=result4[0]
print(totalalbum)


page=totalalbum/10
totalPage=math.ceil(page)
print("\n","tong so trang la:",totalPage)




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
    

















