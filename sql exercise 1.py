import sqlite3

con = sqlite3.connect('cs162.db')

music_data = [
    ("Miley", "Rock", 14),
    ("Dolly", "Country", 123),
    ("Eminen", "HipHop", 98),
    ("Brittany", "Rock", 37)]

genre_data = [
    ("Rock", "Los Angeles"),
    ("Hippie", "Eugene")]

cursor = con.cursor()

# make the tables

# already done
# cursor.execute("create table music_artists (artist text, genre text, number_recordings text)")
# cursor.executemany("insert into music_artists values (?, ?, ?)", music_data)
# con.commit()

# cursor.execute("create table genres (genre text, city text)")
# cursor.executemany("insert into genres values (?, ?)", genre_data)
# con.commit()

# print the tables
# music artists
for row in cursor.execute("select * from music_artists"):
    print(row)
# genres
for row in cursor.execute("select * from genres"):
    print(row)

print("*******")

# unneeded for this week
# cursor.execute("select * from music_artists where genre=:R", {"R": "Rock"})
# rock_search = cursor.fetchall()
# print(rock_search)

cursor.execute("select artist text from music_artists join genres on music_artists.genre = genres.genre")
genre_match = cursor.fetchall()
print(genre_match)

con.close()
