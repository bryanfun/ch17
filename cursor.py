'''
Name: Bryan Banuelos
'''
import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM titles')

columns = [description[0] for description in cursor.description]
print(f'{columns[0]:<15}{columns[1]:<35}{columns[2]:<2}{columns[3]:>10}')

for row in cursor.fetchall():
    print(f'{row[0]:<15}{row[1]:<35}{row[2]:<2}{row[3]:>10}')
connection.close()