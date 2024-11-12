import sqlite3

conn=sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        passwd TEXT NOT NULL,
        age INTEGER NOT NULL,
        deleted BOOL DEFAULT 0
        )
    ''')
conn.commit()

def add_user(name:str, email:str, passwd:str, age:int):
    cursor.execute('''
    SELECT * FROM users WHERE email = ? AND deleted = ?
    ''', (email, False))
    conn.commit()
    user = cursor.fetchall()
    #print(user)

    if len(user) <= 0:
        cursor.execute('''
        INSERT INTO users(name, email, passwd, age) VALUES (?, ?, ?, ?)
        ''', (name, email, passwd, age))
        conn.commit()
        print("added new user")
    else: 
        print("user already exists")
    

def edit_user(email, passwd, newName, newEmail, newPasswd, newAge):
    cursor.execute('''
    SELECT * FROM users WHERE email = ? AND passwd = ? AND deleted = ?
    ''', (email, passwd, False))
    conn.commit()

    users = cursor.fetchall()

    if len(users) <= 0:
        print("User Doesn't Exist")
    else:
       
        cursor.execute('''
        UPDATE users SET name = ?, email = ?, passwd = ?, age = ? WHERE name = ? AND  passwd = ?
        ''', (newName, newEmail, newPasswd, newAge, email, passwd))
        conn.commit()
        print(f"Edited User with email: {email}")



    
    #print(cursor.fetchall())

def read_user(email, passwd):
    cursor.execute('''
    SELECT * FROM users WHERE email = ? AND  passwd = ? AND deleted = ?
    ''', (email, passwd, False))
    conn.commit()

    print(cursor.fetchall())

def delete_user(email, passwd):
    cursor.execute('''
    SELECT * FROM users WHERE email = ? AND passwd = ? AND deleted = ?
    ''', (email, passwd, False))
    conn.commit()

    users = cursor.fetchall()

    if len(users )<= 0:
        print("User Doesn't Exist")
    else:
        cursor.execute('''
        UPDATE users SET deleted = ? WHERE email = ? AND passwd = ?
        ''', (True, email, passwd))
        conn.commit()
        print(f"user with email: {email} deleted.")




command = ""
print("1.read user\n2.new user\n3.edit user\n4.delete user\n5.exit")
while command != "5":
    if command == "1":
        read_user(input("Email: "), input("Password: "))
    elif command == "2":
        add_user(input("Name: "), input("Email: "), input("Passwdord: "), int(input("Age: ")))
    elif command == "3":
        edit_user(input("Old Email: "), input("Old Pass: "), input("New Name: "), input("New Email: "), input("new Password: "), int(input("new age: ")))
    elif command == "4":
        delete_user(input("Email: "), input("Password: "))
    command = input(">: ")


conn.close()
