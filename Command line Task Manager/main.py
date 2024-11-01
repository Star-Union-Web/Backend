Tasks = []

def main_menu():
    while True:
        print()
        print('Command Line TaskManager')
        print()
        print('Choose what you want to do from 1 to 5 :')
        print('1 - Add Task')
        print('2 - View Tasks')
        print('3 - Update Task')
        print('4 - Delete Task')
        print('5 - Exit')
        print()
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
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            update_task()
        elif choice == 4 :
            delete_task()
        else:
            break

def add_task():
    task = {}
    description = input('Enter Your task description : ')
    while description == '':
        print('No task description has been added')
        description = input('Enter Your task description : ')
    task['description'] = description
    pri = ['low','medium','high']
    priority = input('Enter Your task priority (low, Medium, High) : ').lower()
    while priority not in pri:
        priority = input('Please, Enter Your task priority (low, Medium, High) : ').lower()
    task['priority'] = priority
    print('Enter the date of your task: ')
    due_date = []
    day = input('Enter the day number: ')
    while True:
        try :
            day = int(day)
            if day > 31 or day < 1:
                day = input('Please, Enter valid day number : ')
            else:
                break
        except:
            day = input('Please, Enter valid day number : ')
    due_date.append(day)
    month = input('Enter the month number: ')
    while True:
        try :
            month = int(month)
            if month > 12 or month < 1:
                month = input('Please, Enter valid month number : ')
            else:
                break
        except:
            month = input('Please, Enter valid month number : ')
    due_date.append(month)
    year = input('Enter the year number: ')
    while True:
        try :
            year = int(year)
            if year > 9999 or year < 1:
                year = input('Please, Enter valid year number : ')
            else:
                break
        except:
            year = input('Please, Enter valid year number : ')
    due_date.append(year)
    task['due date'] = due_date
    Tasks.append(task)
    print('Task Added Successfully')

def view_tasks():
    if len(Tasks)==0 :
        print()
        print('There is no tasks')
        print()
        return
    counter = 1
    print('All Tasks : ')
    for task in Tasks:
        print(f'''
Task {counter} :-
    Task description : {task['description']},
    Task priority : {task['priority']},
    Task due_date : {task['due date'][0]} / {task['due date'][1]} / {task['due date'][2]}
=====================================
        ''')
        counter+=1

def update_task():
    if len(Tasks)==0 :
        print('There is no tasks to update')
        return
    view_tasks()
    task_index = input('Select the number of the task you want to update : ')
    while True:
        try:
            task_index = int(task_index)
            if task_index > len(Tasks) or task_index < 1:
                task_index = input('Please, Enter valid task number : ')
            else:
                break
        except:
            task_index = input('Please, Enter valid task number : ')
    print('Choose what you want to update in the task : ')
    print('''
1 - description
2 - priority
3 - due date
    ''')
    choice = input('Enter your choice from 1 to 3 : ')
    while True:
        try:
            choice = int(choice)
            if choice > 3 or choice < 1:
                choice = input('Please, Enter valid choice from 1 to 3 : ')
            else:
                break
        except:
            choice = input('Please, Enter a number from 1 to 3 : ')
    if choice == 1:
        description = input('Update Your task description : ')
        while description == '':
            print('No description has been added')
            description = input('Update Your task description : ')
        Tasks[task_index-1]['description'] = description
        print(f'Description for task {task_index} has been updated successfully')
    elif choice == 2:
        pri = ['low', 'medium', 'high']
        priority = input('Enter Your task priority (low, Medium, High) : ').lower()
        while priority not in pri:
            priority = input('Please, Enter Your task priority (low, Medium, High) : ').lower()
        Tasks[task_index-1]['priority'] = priority
        print(f'priority for task {task_index} has been updated successfully')
    else :
        print('Enter the date of your task: ')
        due_date = []
        day = input('Enter the day number: ')
        while True:
            try:
                day = int(day)
                if day > 31 or day < 1:
                    day = input('Please, Enter valid day number : ')
                else:
                    break
            except:
                day = input('Please, Enter valid day number : ')
        due_date.append(day)
        month = input('Enter the month number: ')
        while True:
            try:
                month = int(month)
                if month > 12 or month < 1:
                    month = input('Please, Enter valid month number : ')
                else:
                    break
            except:
                month = input('Please, Enter valid month number : ')
        due_date.append(month)
        year = input('Enter the year number: ')
        while True:
            try:
                year = int(year)
                if year > 9999 or year < 1:
                    year = input('Please, Enter valid year number : ')
                else:
                    break
            except:
                year = input('Please, Enter valid year number : ')
        due_date.append(year)
        Tasks[task_index - 1]['due date'] = due_date
        print(f'date for task {task_index} has been updated successfully')

def delete_task():
    if len(Tasks)==0 :
        print('No Tasks to delete')
        return
    view_tasks()
    choice = input('Select the number of the task you want to delete : ')
    while True:
        try:
            choice = int(choice)
            if choice > len(Tasks) or choice < 1:
                choice = input('Please, Enter valid task number : ')
            else:
                break
        except:
            choice = input('Please, Enter valid task number : ')
    Tasks.pop(choice-1)
    print('Task deleted successfully')

main_menu()