import sqlite3


def show_category_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    print("Available categories: ")
    query = cursor.execute("select * from category")
    for result in query:
        print(f'ID: {result[0]} || Category: {result[1]}')


def show_task_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    print("Available tasks: ")
    query = cursor.execute("select * from task")
    for result in query:
        print(f'ID: {result[0]} || Task: {result[1]}')
