import database
import sqlite3
import validation

tasks = []  # list of tasks that are not saved in database
database_tasks = []  # list of tasks that are saved in database


def input_task() -> dict[str, str, str, int]:
    """
    inputs task data from the user and returns it as a dictionary.

    Returns:
        dict: with structure:
        {
            'title': str,
            'description': str,
            'due_date': str,
            'priority': int
        }
    """
    title = validation.get_valid_title()
    description = input("Enter description: ")
    due_date = validation.get_due_date()
    priority = validation.get_valid_choice(3, "Enter priority from 1 to 3: ")

    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority
    }

    return task


def create_task() -> None:
    """
    Creates a new task and adds it to the CLI.tasks list.

    Global Variables:
        CLI.tasks (list[dict]): List of dictionaries containing task data as temporary data.
    """
    task = input_task()
    tasks.append(task)


def load_tasks(cursor: sqlite3.Cursor) -> None:
    """
    Load tasks from the database and stores them in CLI.database_tasks.

    Args:
        cursor (sqlite3.Cursor): Database cursor for executing SQL queries.

    Global Variables:
        CLI.database_tasks (list[dict]): List of dictionaries containing database tasks data.
    """
    global database_tasks
    list_tuple = database.load_from_database(cursor, '*')
    list_dict = []

    for task in list_tuple:  # convert list of tuple to list of dictionaries
        task_dict = {
            'title': task[0],
            'description': task[1],
            'due_date': task[2],
            'priority': task[3]
        }
        list_dict.append(task_dict)

    database_tasks = list_dict


def view_tasks(cursor: sqlite3.Cursor)-> None:
    """
    Displays the current tasks and prompts the user to save them.
    Args:
        cursor (sqlite3.Cursor): The database cursor used to save and load tasks.

    Note:
        the function recursively calls itself until a valid choice is entered.
    """
    print_tasks()
    
    if tasks == []:  # return here if no new added tasks
        return
     
    choice = input("Do you want to save the tasks? (y/n): ")
    if choice == 'y':
        database.save_tasks(cursor, tasks)
        tasks.clear()  # clear the tasks list after saved to database
        load_tasks(cursor)  # reload the tasks from database
        print("Tasks saved successfully")

    elif choice == 'n':
        return
    
    else:
        print("Invalid choice")
        return view_tasks(cursor)  # recursive call till valid choice is entered
    

def delete_task(cursor: sqlite3.Cursor)-> None:
    """
    Menu to delete a task based on title.
    """
    title = input("Enter title of task to delete: ")
    database.delete_task(cursor, title)


def update_task(cursor: sqlite3.Cursor)-> None:
    """
    Menu to replace a task with new one.
    """
    title = input("Enter title of task to update: ")
    print("Enter new data")
    new_data = input_task()
    database.update_task(cursor, title, new_data)


def print_task(task: dict) -> None:
    """
    Prints the task details in a formatted manner.
    Args:
        task (dict): A dictionary representing a task with keys 'title', 'description', 'due_date', and 'priority'.
    """
    priority = { # priority conversion values
    1: 'Low',
    2: 'Normal',
    3: 'High'
    }

    print(f"Title: {task["title"]}")
    print(f"Description: {task["description"]}")
    print(f"Due date: {task["due_date"]}")

    priority_type = priority[task["priority"]] # convert priority to its nominal value
    print(f"Priority: {priority_type}")


def print_tasks() -> None:
    """
    Prints the tasks in the CLI.tasks and CLI.database_tasks lists.
    """
    
    if database_tasks == []:  # tasks that are saved in database
        print("No saved tasks")
    else:
        print("Saved tasks: ")
        for task in database_tasks:
            print_task(task)
        print()

    if tasks == []:  # tasks that are not saved
        print("No added tasks")
    else:
        print("Added tasks:")
        for task in tasks:
            print_task(task)
    print()
            

def main():
    cursor = database.start_database()

    while True:
        load_tasks(cursor)

        print("Task Manager")
        print("1) Add task")
        print("2) View tasks")
        print("3) Update task")
        print("4) Delete task")
        print("5) Save and exit")
        print("6) Exit without saving")

        choice = validation.get_valid_choice(6, "Enter your choice: ")
        print()


        if choice == 1:
            create_task()

        elif choice == 2:
            view_tasks(cursor)
        
        elif choice == 3:
            update_task(cursor)

        elif choice == 4:
            delete_task(cursor)

        elif choice == 5:
            database.save_tasks(cursor, tasks)
            tasks.clear()
            print("Tasks saved successfully")
            break
        else:
            break

        print()

    database.close_database(cursor)



if __name__ == '__main__':
    main()
