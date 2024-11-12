from API import API
from datahandler import FileHandler

def main():
    response = API.fetchAPI("?results=50")
    data = API.formatData(response)
    file_handler = FileHandler("users.json")
    file_handler.updateFile(data)

if __name__ == "__main__":
    main()