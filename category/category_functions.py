import sqlite3


def show_category_function():
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    print("Available categories: ")
    query = cursor.execute("select * from category")
    for result in query:
        print(f'ID: {result[0]} || Category: {result[1]}')


def create_category_function():
    show_category_function()
    connection = sqlite3.connect('../todo.sqlite3')
    print("Let's create a category?")
    name = input("Enter category name: ")
    print("Category inserted successfully!")

    values = [name]
    sql = 'insert into category (name) values (?)'
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()
    connection.close()


def update_category_function():
    show_category_function()
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()

    def execute():
        category_id = input("Enter the ID of the category you want to update(0 to exit): ")
        if category_id == "0":
            print("Leaving the system... See you soon! :)")
        else:
            name = input("Enter the new category name: ")
            print("Category update successfully!")

            sql = 'update category set name = ? where id = ?'
            values = [name, category_id]
            cursor.execute(sql, values)
            connection.commit()
            connection.close()

    execute()


def delete_category_function():
    show_category_function()
    connection = sqlite3.connect('../todo.sqlite3')
    cursor = connection.cursor()
    delete_category = input("Enter the ID of the category you want to delete: ")
    print('Deleted Successfully.')
    values = [delete_category]
    sql = 'delete from category where id = ?'
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
