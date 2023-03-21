import sqlite3
import task_functions as fun


def completed_tasks_functions():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    fun.show_task_completed()
    opt = input("Write the ID of task you want to set as done: ")
    sql = "update task set status = ? where id = ?"
    print("Task marked as completed")
    valores = [2, opt]
    cursor.execute(sql, valores)
    connection.commit()
    connection.close


completed_tasks_functions()
