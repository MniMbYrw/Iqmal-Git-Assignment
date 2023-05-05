import sqlite3

con = sqlite3.connect('cs162.db')

music_data = [
    ("Miley", "Rock", 14),
    ("Dolly", "Country", 123),
    ("Eminen", "HipHop", 98),
    ("Brittany", "Rock", 37)]

cursor = con.cursor()

cursor.execute("create table music_artists (artist text, genre text, number_recordings text)")
con.commit()

cursor.executemany("insert into music_artists values (?, ?, ?)", music_data)
con.commit()

for row in cursor.execute("select * from music_artists"):
    print(row)

print("*******")

cursor.execute("select * from music_artists where genre=:R", {"R": "Rock"})
rock_search = cursor.fetchall()
print(rock_search)

con.close()
