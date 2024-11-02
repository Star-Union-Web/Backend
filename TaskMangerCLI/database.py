import sqlite3

"""
This module provides functions to interact with a SQLite database for managing tasks.
Functions:
    start_database() -> sqlite3.Cursor:
        Initializes and starts the database connection, creating a 'tasks' table if it does not exist.

    load_from_database(cursor: sqlite3.Cursor, fields: str) -> list:
        Load data from the database by executing a SQL SELECT query to retrieve specified fields from the 'tasks' table.

    save_tasks(cursor: sqlite3.Cursor, list_tasks: list[dict]) -> None:
        Save a list of tasks to the database. Each task is represented as a dictionary with keys 'title', 'description', 'due_date', and 'priority'.
    
    delete_task(cursor: sqlite3.Cursor, title: str) -> None:
        Deletes a task from the database with the given title. Prints "Task not found" if the task is not found.
    
    update_task(cursor: sqlite3.Cursor, title: str, task: dict) -> None:
        Updates a task in the database by deleting the existing task with the given title and saving the new task.
    
    close_database(cursor: sqlite3.Cursor) -> None:
        Closes the database connection.
"""


def start_database()-> sqlite3.Cursor:
    """
    Initializes and starts the database connection, creating a 'tasks' table if it does not exist.

    The 'tasks' table has the following columns:
    - title (TEXT, UNIQUE): The title of the task.
    - description (TEXT): A description of the task.
    - due_date (DATE): The due date of the task.
    - priority (INTEGER): The priority level of the task.

    Returns:
        sqlite3.Cursor: A cursor object to interact with the database.
    """
    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    title TEXT UNIQUE,
    description TEXT,
    due_date DATE,
    priority INTEGER
    )""")
    return cursor


def load_from_database(cursor: sqlite3.Cursor, fields: str)->list:
    """
    Load data from the database.

    This function executes a SQL SELECT query to retrieve specified fields from the 'tasks' table.

    Args:
        cursor (sqlite3.Cursor): The database cursor used to execute the SQL query.
        fields (str): A comma-separated string of field names to be retrieved from the 'tasks' table.

    Returns:
        list: A list of tuples containing the fetched rows from the database.
    """
    cursor.execute(f"SELECT {fields} FROM tasks")
    return cursor.fetchall()


def save_tasks(cursor: sqlite3.Cursor, list_tasks: list[dict])-> None:
    """
    Save a list of tasks to the database.

    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the SQL command.
        list_tasks (list[dict]): A list of dictionaries, where each dictionary represents a task with keys 'title', 'description', 'due_date', and 'priority'.

    Note:
        The program need to deal with the case where a task with the same title already exists in the database.
        else, the program will raise an error.
    """
    cursor.executemany("INSERT INTO tasks VALUES (:title, :description, :due_date, :priority)", list_tasks)
    cursor.connection.commit()


def delete_task(cursor: sqlite3.Cursor, title: str)-> None:
    """
    Deletes a task from the database with the given title.

    Args:
        cursor (sqlite3.Cursor): The database cursor to execute the query.
        title (str): The title of the task to be deleted.

    Note:
        If the task with the given title is not found, an error message "Task not found" will be printed.
    """
    try:
        cursor.execute(f"DELETE FROM tasks WHERE title = ?", (title,))
        cursor.connection.commit()
    except:
        print("Task not found")


def update_task(cursor: sqlite3.Cursor, title: str, task: dict)-> None:
    """
    Updates a task in the database by deleting the existing task with the given title
    and saving the new task.

    Args:
        cursor (sqlite3.Cursor): The database cursor to execute SQL commands.
        title (str): The title of the task to be updated.
        task (dict): The new task data to be saved.
    """
    delete_task(cursor, title)
    save_tasks(cursor, [task])


def close_database(cursor: sqlite3.Cursor)-> None:
    cursor.connection.close()


if __name__ == '__main__':
    cursor = start_database()
    close_database(cursor)