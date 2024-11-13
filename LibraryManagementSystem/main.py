import json

class Book:
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.is_borrowed = False

    def borrow(self):

        if (self.is_borrowed):
            print("This book is already borrowed")
            return

        self.is_borrowed = True

    def return_book(self):

        if not self.is_borrowed:
            print("You don't have the book to return!")
            return

        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):

        for i, b in enumerate(self.books):
            print(f"Book {i}: ")
            print(f"Name: {b.title}")
            print(f"Author: {b.author}")
            print(f"Publication year: {b.pub_year}")
            print(f"Is borrowed: {b.is_borrowed}")

    def borrow_book(self, i):

        if i >= len(self.books):
            print("Book not found")
            return

        self.books[i].borrow()

    def return_book(self, i):

        if i >= len(self.books):
            print("Book not found")
            return

        self.books[i].return_book()

    def save(self):
        with open('library.json', 'w') as f:
            json.dump([{'title': b.title, 'author': b.author, 'pub_year':
            b.pub_year, 'is_borrowed': b.is_borrowed} for b in
            self.books], f)

class ILibrary:
    def __init__(self):
        self.library = Library()

    def add_book(self):
        name = input("Enter book title: ")
        author = input("Enter author: ")
        pub_year = int(input("Enter publication year: "))
        book = Book(name, author, pub_year)

        self.library.add_book(book)

    def borrow_book(self):
        i = int(input("Enter book number: "))
        self.library.borrow_book(i)

    def return_book(self):
        i = int(input("Enter book number: "))
        self.library.return_book(i)

    def view_books(self):
        self.library.view_books()

    def save(self):
        self.library.save()

class Interface:
    def msg(self, msg):
        print(msg)

class ActionChoice:
    def __init__(self, choices, actions):
        self.choices = choices
        self.actions = actions

    def show_choices(self):
        for i, c in enumerate(self.choices):
            print(f"{i+1}) {c}.")
        
    def take_action(self):
        self.show_choices()
        action = 0
        while action < 1 or action > len(self.choices):
            action = int(input("Enter your choice: "))
            return self.actions[action-1]()

def exit():
    return False

if __name__ == "__main__":

    lib = ILibrary()
    while True:


        a = ActionChoice(["Add book", "View books", "Borrow books", "Return book", "Save", "Exit"], [lib.add_book, lib.view_books, lib.borrow_book, lib.return_book, lib.save, exit])
        action = a.take_action()
    
        if action is False:
            break