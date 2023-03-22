import sqlite3


def tasks_per_day_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    print("Let's filter the tasks by date.")
    print("These are the dates that have a task included:")
    available_dates = '''
    select date from task
    '''
    query_one = cursor.execute(available_dates)
    for result in query_one:
        print(result)
    tasks_per_day = input("Do you want to know the tasks of which date? (format: mm/dd/yyyy) ")
    date = [tasks_per_day]
    query_two = 'select * from task where date = ?'
    query_data = cursor.execute(query_two, date)
    for result in query_data:
        print(result)


tasks_per_day_function()
