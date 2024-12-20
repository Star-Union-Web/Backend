import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

def add_user(name, address, email):
     
     cursor.execute(
        '''
        INSERT INTO users (name, address, email) VALUES (?, ?, ?)
        ''', 
        (name, address, email))
     conn.commit()

def list_store_items():
     cursor.execute('''
    SELECT * FROM items
    ''')
     conn.commit()
     itms = cursor.fetchall()
     print(itms)

def list_orders():
    cursor.execute('''
        SELECT * FROM orders
    ''')
    conn.commit()
    print(cursor.fetchall)

def add_to_order():
     cursor.execute('''
        INSERT INTO orders
    ''')



def main():
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   address TEXT NOT NULL,
                   email TEXT NOT NULL
                   )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
                   order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   time TEXT NOT NULL,
                   user_id INTEGER,
                   item_id INTEGER,
                   FOREIGN KEY (user_id) REFERENCES users(user_id),
                   FOREIGN KEY (item_id) REFERENCES items(item_id)
                   )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items(
                   item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price INTEGER NOT NULL
                   )
    ''')

    cursor.execute('''
    INSERT INTO items (name, price) VALUES (?, ?)
''', ("khodar", 700))
    conn.commit()
   
    
    userName = input("Username: ")
    cursor.execute('''
    SELECT * FROM users WHERE name = ?
''', (userName,))
    baba = cursor.fetchone()
    print(baba)

    if not baba:
         address = input("address: ")
         email = input("email: ")
         add_user(userName, address, email)


    command = ""
    while command != "6":
        print("1. Add Item to Order")
        print("2. View store items")
        print("3. Remove item from order")
        print("4. Comfirm order")
        print("5. view your orders")
        print("6. exit")

        if command == "2":
             list_store_items()




        command = input(">: ")





    conn.close()

    return 0

main()