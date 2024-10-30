import sqlite3

def initiate_db():
    connection = sqlite3.connect("not_telegram.dp")
    cursor = connection.cursor()

    cursor.execute("Create Table If Not Exists Products(id Integer Primary Key, title Text Not Null, description Text, price Integer Not Null)")

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("not_telegram.dp")
    cursor = connection.cursor()

    cursor.execute("Select * From Products")
    data = cursor.fetchall()

    connection.commit()
    connection.close()

    return data
    



