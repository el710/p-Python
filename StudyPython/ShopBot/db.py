"""
    SQL DataBases ....

"""
import sqlite3

import random


connection = sqlite3.connect("database.dp")
cursor = connection.cursor()

cursor.execute('''
Create Table If Not Exists Users(
               id Int,
               username Text,
               first_name Text,
               block Int
               )
''')

def add_user(user_id, username, first_name):
    check_user = cursor.execute("Select * From Users Where id = ?", (user_id, ))
    if check_user.fetchone()[0] is None:
        cursor.execute(f"Insert Into Users Values('{user_id}', '{username}', '{first_name}', 0)", )
    connection.commit()


connection.commit()
connection.close()
