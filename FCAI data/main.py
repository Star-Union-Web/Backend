# sqlite3 library for database , os library to determine the directory of the database file exactly
import sqlite3 , os 
# coloring error messages
from rich import print
# connecting the database file or creating it if it does not exist
db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'students.db'))

cur = db.cursor()
# cur.execute("DROP TABLE student")
#creating a student table if it does not exist
cur.execute("CREATE TABLE IF NOT EXISTS student(name TEXT NOT NULL, id INTEGER PRIMARY KEY ,grade TEXT NOT NULL)")
#committing the changes to database file
db.commit()





# function to view all students in database file
def viewStudents():
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    if len(data):
        count = 1
        for row in data : 
            print(count, " - ")
            count+=1
            print(f'   name : {row[0]}\n   id : {row[1]}\n   grade : {row[2]}')
    else:
        print('There is no students added')



#function to add a student into database file
def addStudent():
    # the admin password
    password = input('Enter your password : ')
    if password=='admin' : 
        #name input and its validating
        name = input('Enter your full name : ')
        while name == '':
            print('Name should not be empty.')
            name = input('Enter your full name : ')
        #id input and its validating
        id = input('Enter your id (8 digits): ')
        while True:
            try:
                id = int(id)
                if id < 1 or id > 99999999 or len(str(id))!=8:
                    print('The id should be positive integer contains 8 digits.')
                    id = input('Enter your id (8 digits): ')
                else:
                    cur.execute("SELECT 1 FROM student WHERE id = (?)",(id,))
                    if cur.fetchone():
                        print('this id already exists.')
                        id = input('Enter your id (8 digits): ')
                    else: break
            except:
                print('the id should be a number')
                id = input('Enter your id (8 digits): ')
        #grade input and its validating
        grades = ['excellent','very good','good','failed']
        grade = input('Enter your grade(excellent, very good, good, failed) : ').lower()
        while grade not in grades : 
            print('that\'s not a valid grade.')
            grade = input('Enter your grade(excellent, very good, good, failed) : ').lower()
        # inserting the student into the database file
        cur.execute("INSERT INTO student(name,id,grade) VALUES(?,?,?)", (name,id,grade))
        #committing the changes
        db.commit()
        print('[green]The student added successfully[/green]')
    else:
        print('[bold red]you are not admin, you don\'t have the authority to delete a student. [/bold red]')


def deleteStudent():
    # the admin password
    password = input('Enter your password : ')
    if password=='admin' : 
        viewStudents()
        #id input and its validating
        id = input('Enter the id of the student you want to delete (8 digits): ')
        while True:
            try:
                id = int(id)
                if id < 1 or id > 99999999 or len(str(id))!=8:
                    print('The id should be positive integer contains 8 digits.')
                    id = input('Enter the id of the student you want to delete (8 digits): ')
                else:
                    cur.execute("SELECT 1 FROM student WHERE id = ?",(id,))
                    if cur.fetchone():
                        break
                    else:
                        print('this id does not exist.')
                        id = input('Enter the id of the student you want to delete (8 digits): ')
            except:
                print('the id should be a number')
                id = input('Enter the id of the student you want to delete (8 digits): ')
        cur.execute("DELETE FROM student WHERE id = ?",(id,))
        db.commit()
        print(f'[green]student with id "{id}" is deleted successfully. [/green]')
    else:
        print('[bold red]you are not admin, you don\'t have the authority to delete a student. [/bold red]')




def updateStudentInfo():
    global cur , db
    # the admin password
    password = input('Enter your password : ')
    if password=='admin' :
        viewStudents()
        data = ()
        #id input and its validating
        id = input('Enter the id of the student you want to update his info (8 digits): ')
        while True:
            try:
                id = int(id)
                if id < 1 or id > 99999999 or len(str(id))!=8:
                    print('The id should be positive integer contains 8 digits.')
                    id = input('Enter the id of the student you want to update his info (8 digits): ')
                else:
                    cur.execute("SELECT * FROM student WHERE id = (?)",(id,))
                    data = cur.fetchone()
                    if data:
                        break
                    else:
                        print('this id does not exist.')
                        id = input('Enter the id of the student you want to update his info (8 digits): ')
            except:
                print('the id should be a number')
                id = input('Enter the id of the student you want to update his info (8 digits): ')
        print()
        print(f'   name : {data[0]}\n   id : {data[1]}\n   grade : {data[2]}')
        print()
        print("#"*50)
        print(f'Select which of these you want to update for the student with id {id}.')
        print('1 - name')
        print('2 - grade')
        print("[bright_yellow]NOTE : the id cannot be updated as it's unique for all students.[/bright_yellow]")
        choice = input('Enter your choice : ')
        while choice not in ['1','2'] : 
            print('invalid choice.')
            choice = input('Please, Enter valid choice 1 or 2 : ')
        if choice == '1':
            #name input and its validating
            name = input('Enter your full name : ')
            while name == '':
                print('Name should not be empty.')
                name = input('Enter your full name : ') 
            cur.execute('UPDATE student SET name = ? WHERE id = ?',(name,id,))
            db.commit()
            print('[green]Name updated successfully.[/green]')
        else:
            #grade input and its validating
            grades = ['excellent','very good','good','failed']
            grade = input('Enter your grade(excellent, very good, good, failed) : ').lower()
            while grade not in grades : 
                print('that\'s not a valid grade.')
                grade = input('Enter your grade(excellent, very good, good, failed) : ').lower()
            cur.execute('UPDATE student SET grade = ? WHERE id = ?',(grade,id,))
            db.commit()
            print('[green]Grade updated successfully.[/green]')
    else:
        print('[bold red]you are not admin, you don\'t have the authority to delete a student. [/bold red]')

#the menu function
def mainMenu():
    while True:
        print('#'*50)
        print('FCAI Students Menu')
        print('#'*50)
        print('Choose what you want to do from 1 to 5 :')
        print('1 - Add student')
        print('2 - View students')
        print('3 - Update student')
        print('4 - Delete student')
        print('5 - Exit')
        print()
        # choice input and its validation
        choice = input('Enter your choice from 1 to 5 : ')
        while True:
            try :
                choice = int(choice)
                if choice > 5 or choice < 1:
                    choice = input('Please, Enter valid choice from 1 to 5 : ')
                else:
                    break
            except:
                choice = input('Please, Enter a number from 1 to 5 : ')
        if choice==1:
            addStudent()
        elif choice==2:
            viewStudents()
        elif choice==3:
            updateStudentInfo()
        elif choice == 4 :
            deleteStudent()
        else:
            print("[bold cyan]Thank you for using my program![/bold cyan]")
            break


mainMenu()

#closing the file
db.close()