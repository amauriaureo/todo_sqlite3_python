import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table category (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20)
)

'''

cursor.execute(sql)
connection.commit()
connection.close()
