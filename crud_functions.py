import sqlite3
connection = sqlite3.connect("prod.db")
cursor = connection.cursor()
def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
''')
    for i in range(1, 5):
        cursor.execute(" INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)", (f"{i}", f"Продукт {i}", f"Описание {i}", f"{i*100}"), )
def get_all_products():
    cursor.execute(" SELECT * FROM Products", )
    products = cursor.fetchall()
    return products

#initiate_db()
#connection.commit()
#connection.close()
