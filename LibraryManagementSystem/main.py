from library import Library, Book
from validation import Validation
from ORM import ORM


class Interface:
    max_books = 3

    def __init__(self):
        ORM.__init__()
        self.library = Library()
        self.list_borrowed = self.library.get_books(isBorrowed=True)

    def add_book(self):
        """
        Takes user input for book details, create book object and adds the book to the library
        """
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = Validation.get_valid_date("Enter publication year (YYYY-MM-DD): ")
        isBorrowed = False
        book = Book(title, author, publication_year, isBorrowed)
        self.library.add_book(book)

    def borrow_book(self):
        """
        Takes user input for book title and borrows the book
        """
        if len(self.list_borrowed) >= self.max_books:
            print("You have reached the maximum number of books you can borrow")
        else:        
            title = input("Enter title: ")
            self.list_borrowed.append(self.library.borrow_book(title))

    def return_book(self):
        """
        Takes user input for book title and returns the book
        """
        title = input("Enter title: ")
        book = self.library.get_book(title)
        if book is None:
            print("Book not found")
        else:
            book.return_book()
            self.list_borrowed.remove(book)

    def run_interface(self):
        """
        Runs the interface for the library
        """
        while True:
            print("1. Add a book")
            print("2. View all books")
            print("3. View borrowed books")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. Exit")
            choice = Validation.get_valid_choice(6, "Enter choice: ")

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.library.view_books()
            elif choice == 3:
                for book in self.list_borrowed:
                    print(book)
            elif choice == 4:
                self.borrow_book()
            elif choice == 5:
                self.return_book()
            elif choice == 6:
                break


if __name__ == "__main__":
    interface = Interface()
    interface.run_interface()
