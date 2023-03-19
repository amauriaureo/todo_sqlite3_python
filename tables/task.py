import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()


sql = '''
create table task (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(20),
    date VARCHAR(20),
    status VARCHAR(20),
    category_id INT NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category(id)
)

'''

cursor.execute(sql)
connection.commit()
connection.close()
