import sqlite3

conn = sqlite3.connect('chinook.db')
print ("Opened database successfully", conn)

cursor3 = conn.execute("SELECT * FROM genres LIMIT 3")
result3 = cursor3.fetchone()
print ("\n", "Get rows by fetch one", type(result3), result3)


cursor2 = conn.execute("SELECT * FROM genres LIMIT 3")
result2 = cursor3.fetchall()
print ("\n", "Get rows by fetch all", type(result2), result2)

print ("\n", "Get rows by Iterable")

cursor1 = conn.execute("SELECT * FROM genres LIMIT 3")
for row in cursor1:
   print ("row = ", row[0], row[1])

conn.close()


connNamming = sqlite3.connect('chinook.db')
connNamming.row_factory = sqlite3.Row

print ("\n", "Get rows by Iterable naming")
cursorNaming = connNamming.execute("SELECT * FROM genres LIMIT 3")
for row in cursorNaming:
   print ("row = ", row["GenreId"], row["Name"])

connNamming.close()