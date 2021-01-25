import sqlite3

#conn = sqlite3.connect('chinook.db', isolation_level= None) # auto comit isolation_level= None
conn = sqlite3.connect('chinook.db')
print ("Opened database successfully", conn)
conn.execute("INSERT INTO genres VALUES (125, 'genre 125')")

conn.execute("INSERT INTO genres VALUES (?,?)", (126, "genre 126"))

conn.execute("INSERT INTO genres VALUES (?,?)", [1278, "genre 127"])

conn.execute("INSERT INTO genres VALUES (:id, :name)", { "id": 128, "name": "genre 128"})

conn.commit()

conn.close()