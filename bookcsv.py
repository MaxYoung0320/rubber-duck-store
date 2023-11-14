import csv
import random
import sqlite3
import sys

try:
    connection = sqlite3.connect("db.db")

    print("Successful Connection")

except:
    print("Failed Connection")
    sys.exit()

cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' ;")

table_names = cursor.fetchall()

print("Table Names: ")
for table_name in table_names:
    print(table_name)

# book_genres = ["fiction", "non-fiction", "fantasy", "horror", "historical", "drama", "folklore", "romanace", "young adult", "poetry"]
# with open("books.csv") as f:
#     next(f)
#     for line in f:
#         isbn = line.split(',')[5] # isbn
#         title = line.split(',')[1] # title
#         author = line.split(',')[2] # author
#         pages = line.split(',')[7] # pages
#         release_date = line.split(',')[10] # release date
#         genre = random.choice(book_genres) # genre
#         stock = random.randint(0, 50) # stock

#         cursor.execute(f"INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('{isbn}', '{title}', '{author}', '{genre}', '{pages}', '{release_date}', '{stock}')")
#         connection.commit()
#         break