"""
    SQL DataBases with sqlite3....

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
    if use 'Int' instead 'Integer' in <Create> that will make null meanings in <id> fields
"""
"""
    make an index...
"""
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

"""
    Add records...
""" ###                              which columns           maket of data           tuple of means
# cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", ("newuser", "ex@gmail.com", "25"))

# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES(?, ?, ?)", (f"newuser_{i}", f"ex_{i}@gmail.com", random.randint(25, 50)))

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
    take count of records...
"""
cursor.execute("Select Count(*) From Users")
total_1 = cursor.fetchone()[0]
print(f"Rec count: {total_1}")

## how much records with age > 28
# cursor.execute("Select Count(*) From Users Where age > ?", (28, ))

## middle age...
cursor.execute("Select SUM(age) From Users")
sum_age = cursor.fetchone()[0]
cursor.execute("Select COUNT(*) From Users")
all_count = cursor.fetchone()[0]
print(f"Mid age : {sum_age / all_count}")
## check out...
cursor.execute("Select AVG(age) From Users")
avg_age = cursor.fetchone()[0]
print(f"Avg age : {avg_age}")

## min - max
cursor.execute("Select Min(age) From Users")
min_age = cursor.fetchone()[0]
cursor.execute("Select Max(age) From Users")
max_age = cursor.fetchone()[0]
print(f"Min-Max: {min_age} - {max_age}")


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
