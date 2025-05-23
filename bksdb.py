"""
Name: Bryan Banuelos
"""
import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10

print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))
print() 

print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print()

cursor = connection.cursor()
cursor.execute("INSERT INTO authors (id, first, last) VALUES (9, 'Hello', 'Deitel')")
cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright) VALUES ('0124289346', 'Advanced Python Programming', '2', '2025')""")
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (9, '0124289346')") 

print(pd.read_sql("""SELECT authors.first, authors.last, titles.title, titles.edition, titles.copyright, 
                  titles.isbn FROM titles
                  INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
                  INNER JOIN authors ON authors.id = author_ISBN.id
                  WHERE authors.id = 9""", connection))

connection.close()