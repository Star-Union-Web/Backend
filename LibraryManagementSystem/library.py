import datetime as dt
from ORM import ORM


class Book(ORM):
    title: str
    author: str
    publication_year: dt.date
    isBorrowed: bool

    def __init__(self, title: str, author: str, publication_year: dt.date, isBorrowed: bool):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isBorrowed = isBorrowed

    def borrow(self)-> None:
        """updates the isBorrowed to True"""
        self.isBorrowed = True
        self.update("isBorrowed", True)
    
    def return_book(self)-> None:
        """updates the isBorrowed to False"""
        self.isBorrowed = False
        self.update("isBorrowed", False)
    
    def __str__(self)-> str:
        return f"{self.title} by {self.author}\nPublished: ({self.publication_year})"
    
    def __repr__(self)-> str:
        return f"Book id: {self._id}\n{self.title} by {self.author}\nPublished: ({self.publication_year})\nBook is {'Borrowed' if self.isBorrowed else 'Available'}"


class Library:
    def __init__(self):
        self.books = Book.get_objects()
        
    def add_book(self, book: Book):
        """
        Args:
            book (Book): The book object
        Takes a book object and saves it to the library and database
        """
        book.save()
        self.books.append(book)

    def get_books(self, isBorrowed: bool) -> list:
        """
        Args:
            isBorrowed (bool): The status of the books to return
        Returns:
            list: A list of books with the specified isBorrowed status

        """
        return [book for book in self.books if book.isBorrowed == isBorrowed]

    def view_books(self):
        """
        Prints all the books to the library with additional information
        """
        if self.books == []:
            print("No books in the library")
            return
        
        [print(repr(book)) for book in self.books]

    def get_book(self, title: str) -> Book:
        """
        Args:
            title (str): The title of the book to return
        Returns:
            Book: The book object with the specified title
        """
        for book in self.books:
            if book.title == title:
                return book

    def borrow_book(self, title: str)-> Book | None: 
        """
        Args:
            title (str): The title of the book to borrow
        Returns:
            Book: The borrowed book object
            None: If the book is already borrowed or not found
        Error:
            If the book is already borrowed, prints "{book.title} is already borrowed"
            If the book is not found, prints "Book: {title} not found"
            """ 
        for book in self.books:
            if book.title == title:
                if book.isBorrowed:
                    print(f"{book.title} is already borrowed")
                else:
                    book.borrow()
                    return Book
                return
        print(f"Book: {title} not found")
    
    def return_book(self, title: str) -> None:
        """
        Args:
            title (str): The title of the book to return
        Returns:
            None
        Error:
            If the book is not found, prints "Book: {title} not found"
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book: {title} not found")


if __name__ == "__main__":
    ORM.migrate()
