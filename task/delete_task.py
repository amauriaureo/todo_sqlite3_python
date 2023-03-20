import sqlite3
import task_functions as fun


def delete_task_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()

    fun.show_task_function()

    available_tasks = "select * from task"
    query = cursor.execute(available_tasks)
    for result in query:
        result

    delete_task = input("Enter the ID of the task you want to delete (0 to exit): ")
    if delete_task == "0":
        print("Exiting the delete task service.")
    else:
        print(f'Task "{result[1]}" successfully removed.')
    values = [delete_task]

    sql = 'delete from task where id = ?'
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


delete_task_function()
