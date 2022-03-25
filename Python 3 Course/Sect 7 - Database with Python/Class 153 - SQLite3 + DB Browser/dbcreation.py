import sqlite3

connection = sqlite3.connect('phonebook.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS phonebook ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'phone TEXT UNIQUE'
               ')')

connection.commit()
