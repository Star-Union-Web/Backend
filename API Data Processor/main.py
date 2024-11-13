from API import API
from datahandler import FileHandler

def printData(data):
    for user in data:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        print(f"Address: {user['address']}")
        print()

def takeNumberUsers():
    try:
        number = int(input("Enter the number of users you want to fetch: "))
        if number < 1 or number > 5000:
            raise ValueError
        return number
    except ValueError:
        print("Invalid number of users. Please enter a number between 1 and 5000")
        return takeNumberUsers()

def main():
    number_of_users = takeNumberUsers()
    response = API.fetchAPI(f"?results={number_of_users}")
    data = API.formatData(response)
    printData(data)
    file_handler = FileHandler("users.json")
    file_handler.updateFile(data)

if __name__ == "__main__":
    main()