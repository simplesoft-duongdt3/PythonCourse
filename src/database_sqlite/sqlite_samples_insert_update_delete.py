import sqlite3

conn = sqlite3.connect('chinook.db', isolation_level= None) # auto comit isolation_level= None
print ("Opened database successfully", conn)
conn.execute("INSERT INTO genres VALUES (26,'Opera 2')")
# conn.commit()

conn.close()