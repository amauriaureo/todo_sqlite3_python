import sqlite3
import task_functions as fun


def update_task_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()

    fun.show_task_function()

    update = input("Enter the ID of the task you want to update: ")
    name = input("Enter the name of the task: ")
    date = input("Enter the task date: ")

    status = int(input('Enter the task Status (Enter "1" for "In progress" or "2" for "Completed": '))

    fun.show_category_function()

    category_id = input("Enter the ID of the category the task belongs to: ")

    print("Task successfully updated!")

    sql = 'update task set name = ?, date = ?, status = ?, category_id = ? where id = ? '

    values = [name, date, status, category_id, update]
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


update_task_function()
