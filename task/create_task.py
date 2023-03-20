import sqlite3
import task_functions as fun


def create_task_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()

    print("Write task data: ")
    name = input("Name: ")
    date = input("Date: ")
    status = 1

    fun.show_category_function()

    category_id = input("Select the category ID this task belongs to: ")

    print("Task entered successfully!")

    values = [name, date, status, category_id]
    sql = 'insert into task (name, date, status, category_id) values (?, ?, ?, ?)'
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()


create_task_function()
