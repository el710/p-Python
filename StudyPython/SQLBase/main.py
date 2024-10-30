"""
    SQL DataBases ....

"""

import sqlite3

import random

"""
    import module_14...
"""

connection = sqlite3.connect("database.dp")
cursor = connection.cursor()

"""
    init table Users in database "database.dp"
"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER
               )
''')

"""
    make an index...
"""
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

"""
    Add records...
""" ###                              which columns           maket of data           tuple of means
# cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", ("newuser", "ex@gmail.com", "25"))

for i in range(30):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", (f"newuser_{i}", f"ex_{i}@gmail.com", random.randint(25, 50)))

"""
    Read data...
"""
## take all records...
cursor.execute("SELECT * FROM Users")
## take records with age > 29
# cursor.execute("SELECT username, age FROM Users WHERE age > ?", (29, ))
## take all with sorting by age
# cursor.execute("SELECT username, age FROM Users GROUP BY age")
# cursor.execute("select username, age from Users group by age") -- also works


users = cursor.fetchall()
for user in users:
    print(f"{user} - {type(user)}")


"""
    Edit data...
"""
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))

"""
    Delete records...
"""
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser", ))




"""
    save data in base - !!! without this there is nothing will be in table
"""
connection.commit()

"""
    close connection - !!! without this there is nothing will be in table
"""
connection.close()
