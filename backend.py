import sqlite3

def connection():
  conn=sqlite3.connect('book.db')
  conn.execute('CREATE TABLE if not exists library (id integer PRIMARY KEY AUTOINCREMENT, title text not null, author text not null, year integer, isbn text)')
  conn.commit()
  conn.close()

connection()
