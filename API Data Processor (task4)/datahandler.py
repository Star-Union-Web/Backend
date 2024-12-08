import json

class FileHandler:
    """
    Attributes:
        filename (str): The path to the JSON file to be loaded.
        data (dict): The contents of the JSON file.
        dict_name (str): The key in the JSON file that contains the data.
    
    Methods:
        loadFile: Loads a JSON file and returns its contents as a dictionary.
        updateFile: Updates the file with new data.

    A class to handle reading and writing data to a JSON file.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.loadFile(filename)
        self.dict_name = "users" 
        
    def loadFile(self, filename: str) -> dict:
        """
        Loads a JSON file and returns its contents as a dictionary.
        Args:
            filename (str): The path to the JSON file to be loaded.
        Returns:
            dict: The contents of the JSON file.
        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: If there is an error loading data from the file.
        """
        try:
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")

        except Exception as e:
            raise Exception("Error loading data from file. ", e)

    def updateFile(self, new_data: list[dict]):
        """
        Updates the file with new data.

        This method appends new data to the existing data stored in the file specified by `self.filename`.
        The data is expected to be a list of dictionaries.

        Args:
            new_data (list[dict]): A list of dictionaries containing the new data to be added.

        Raises:
            Exception: If there is an error writing data to the file, an exception is caught and an error message is printed.
        """
        self.data[self.dict_name] += new_data
        try:
            with open(self.filename, "w") as file:
                json.dump(self.data, file, indent=4)
                print("Data written to file successfully.")
        except Exception as e:
            print("Error writing data to file. ", e)

        