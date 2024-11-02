from typing import Optional
import datetime
import CLI


def validate_and_return_date(date: str) -> Optional[datetime.date]:
    """
    Validates a date string and returns a date object if valid.
    This function takes a date string in the format 'YYYY-MM-DD' and attempts to
    convert it to a `datetime.date` object. If the date is valid and not in the past,
    it returns the date object. If the date is invalid or in the past, it returns None.
    Args:
        date (str): The date string to validate.
    Returns:
        datetime.date or None: The validated date object or None if the date is invalid or in the past.
    """
    try :
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if date < datetime.date.today():
            return None
        else:
            return date
        
    except ValueError:
        return None
   
   
def get_due_date()-> datetime.date:
    """
    Prompts the user to enter a due date in the format 'yyyy-mm-dd' and validates the input.
    Returns:
        datetime.date: The validated due date entered by the user.
    Note:
    If the input is invalid, the function will print an error message and recursively prompt the user to enter the due date again until a valid date is provided.
    """
    due_date = input("Enter due date (yyyy-mm-dd): ")
    due_date = validate_and_return_date(due_date)

    if due_date == None:
        print("Incorrect due date")
        return get_due_date()   
    else:
        return due_date
 
    
def get_valid_choice(num_choices: int, message: str) -> int:
    """
    Prompts the user to enter a valid choice within a specified range.

    Args:
        num_choices (int): The number of valid choices available.
        message (str): The message to display when prompting the user for input.

    Returns:
        int: The user's valid choice as an integer.

    Note:
    If the input is invalid, prints "Invalid choice" and calls itself recursively until a valid choice is entered.
    """
    try:
        choice = int(input(message))
        if choice < 1 or choice > num_choices:
            print("Invalid choice")
            return get_valid_choice(num_choices, message)
        else:
            return choice
    except :
        print("Invalid choice")
        return get_valid_choice(num_choices, message)
    

def get_valid_title() -> str:
    """
    Prompts the user to enter a task title and validates it.
    The function ensures that the title is not empty and does not already exist
    in either the `CLI.database_tasks` or `CLI.tasks` lists. If the title is 
    invalid, it prompts the user to enter a new title until a valid one is provided.
    Returns:
        str: A valid task title.
    """
    title = input("Enter task title: ")

    if title == "":
        print("Title cannot be empty")
        return get_valid_title()
    
    for task in CLI.database_tasks:
        if title == task[0]:
            print("Title already exists")
            return get_valid_title()

    for task in CLI.tasks:
        if title == task['title']:
            print("Title already exists")
            return get_valid_title()    

    return title