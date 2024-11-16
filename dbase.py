import sqlite3

## create table...

## make indexes...

"""
    Add records...
""" ###                              which columns           maket of data           tuple of means
cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", ("newuser", "ex@gmail.com", "25"))

for i in range(30):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", (f"newuser_{i}", f"ex_{i}@gmail.com", "25"))

"""
    Edit data...
"""
cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))

"""
    Delete records...
"""
cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser", ))
