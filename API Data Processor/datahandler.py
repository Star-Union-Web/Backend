import json


class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self.loadFile(filename)
        self.dict_name = "users" 
        
    def loadFile(self, filename: str) -> dict:
        try:
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")

        except Exception as e:
            raise Exception("Error loading data from file. ", e)

    def updateFile(self, new_data: list[dict]):
        self.data[self.dict_name] += new_data
        try:
            with open(self.filename, "w") as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print("Error writing data to file. ", e)

        