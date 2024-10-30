import sqlite3

connection = sqlite3.connect("not_telegram3.dp")
cursor = connection.cursor()

cursor.execute("""Create Table If Not Exists Users(id integer primary key, username text not null, email text not null, age integer, balance integer not null)""")


for i in range(1, 11):
    cursor.execute("Insert Into Users (username, email, age, balance) Values(?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

for i in range(1, 11, 2):
    cursor.execute("Update Users Set balance = ? Where id = ?", (500, i))

for i in range(1, 11, 3):
    cursor.execute("Delete From Users Where id = ?", (i, ))

for i in range(11):
    cursor.execute("Select username, email, age, balance From Users Where age != 60")

users = cursor.fetchall()
for user in users:
    print(f"Name: {user[0]} | Email: {user[1]} | Age: {user[2]} | Balance: {user[3]}")



connection.commit()
connection.close()