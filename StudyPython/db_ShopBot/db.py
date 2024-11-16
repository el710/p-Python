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
        cursor.execute(f"Insert Into Users Values('{user_id}', '{username}', '{first_name}', 0)" )
    connection.commit()


def show_users():
    user_list = cursor.execute("Select * From Users")
    message = ""
    for user in user_list:
        message += f"{user[0]} @{user[1]} {user[2]} \n"
    connection.commit()
    return message

def show_stat():
    count_users = cursor.execute("Select Count(*) From Users").fetchone()
    connection.commit()
    return count_users[0]

def add_block(input_id):
    cursor.execute(f"Update Users Set block = ? Where id = ?", (1, input_id))
    connection.commit()

def remove_block(input_id):
    cursor.execute(f"Update Users Set block = ? Where id = ?", (0, input_id))
    connection.commit()

def check_block(user_id):
    users = cursor.execute(f"Select block Form Users Where id = ?", (user_id, )).fetchone()
    connection.commit()
    return users[0]


connection.commit()
connection.close()
