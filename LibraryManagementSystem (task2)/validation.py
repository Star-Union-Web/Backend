import datetime


class Validation:
    
    @staticmethod
    def _validate_and_return_date(date: str) -> datetime.date | None:
        """
        Validates a date string and returns a date object if valid.
        This function takes a date string in the format 'YYYY-MM-DD' and attempts to
        convert it to a `datetime.date` object. If the date is valid,
        it returns the date object. If the date is invalid, it returns None.
        Args:
            date (str): The date string to validate.
        Returns:
            datetime.date or None: The validated date object or None if the date is invalid or in the past.
        """
        try :
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            return date

        except ValueError:
            return None
    
    @staticmethod
    def get_valid_date(message: str)-> datetime.date:
        """
        Prompts the user to enter a due date in the format 'yyyy-mm-dd' and validates the input.
        Returns:
            datetime.date: The validated due date entered by the user.
        Note:
        If the input is invalid, the function will print an error message and recursively prompt the user to enter the due date again until a valid date is provided.
        """
        due_date = input(message)
        due_date = Validation._validate_and_return_date(due_date)

        if due_date == None:
            print("Incorrect due date")
            return Validation.get_valid_date()   
        else:
            return due_date
    
    @staticmethod
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
                return Validation.get_valid_choice(num_choices, message)
            else:
                return choice
        except :
            print("Invalid choice")
            return Validation.get_valid_choice(num_choices, message)

