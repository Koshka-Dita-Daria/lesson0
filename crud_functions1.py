import sqlite3
connection = sqlite3.connect("product.db")
cursor = connection.cursor()
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
''')

def add_user(username, email, age, balance = 1000):
    check_user = cursor.execute(" SELECT * FROM Users WHERE username = ?", (username, ))
    if check_user.fetchone() is None:
        cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"{username}", f"{email}", f"{age}", f"{balance}"), )
    connection.commit()
def is_included(username):
    kol = cursor.execute(" SELECT COUNT(*) FROM Users WHERE username = ?", (username, ), ).fetchone()
    if kol[0] != 0:
        return False
    else:
        return True
    connection.commit()
def get_all_products():
    cursor.execute(" SELECT * FROM Users", )
    products = cursor.fetchall()
    return products


#initiate_db()
#connection.commit()
#connection.close()