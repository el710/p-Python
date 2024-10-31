import sqlite3

db_name = ""

def open_db():
    global db_name
    connection = sqlite3.connect(db_name)
    return  connection, connection.cursor()

def close_db(connection):
    connection.commit()
    connection.close()


def initiate_db(name):
    global db_name
    db_name = name
    connection, cursor = open_db()
    
    idc = cursor.execute('''Create Table If Not Exists 
                   Users(
                    id Integer Primary Key, 
                    username Text Not Null, 
                    email Text Not Null, 
                    age integer, 
                    balance Integer Not Null
                  )
    ''')
    # print(f"make Users - {idc}")

    idc = cursor.execute("Create Table If Not Exists Products (id Integer Primary Key, title Text Not Null, description Text, price Integer Not Null)")
    # print(f"make Products - {idc}")

    close_db(connection)
    
def is_included(username):
    connection, cursor = open_db()
    id = cursor.execute("Select username From Users Where username = ?", (username, )).fetchone()
    close_db(connection)
    return id != None

def add_user(username, email, age):
    if not is_included(username):
        connection, cursor = open_db()
        cursor.execute("Insert Into Users (username, email, age, balance) Values(?, ?, ?, 1000)", (username, email, age))
        close_db(connection)


    



def add_product(list):
    connection, cursor = open_db()
            
    for item in list:
        print(f"save: {item}")
        cursor.execute("Insert Into Products (title, description, price) Values(?, ?, ?)", item)
        
    close_db(connection)


def get_all_products():
    connection, cursor = open_db()

    cursor.execute("Select * From Products")
    data = cursor.fetchall()

    close_db(connection)

    return data
    



