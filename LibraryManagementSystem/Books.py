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

    def __str__(self):
        return f"{self.title} by {self.author}, published: ({self.publication_year})"
    
    def __repr__(self):
        return f"{self.title} by {self.author}, published: ({self.publication_year})"


if __name__ == "__main__":
    ORM.__init__()
    ORM._migrate()
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", dt.date(1925, 4, 10), False)
    book.save()
    book = Book("The Catcher in the Rye", "J.D. Salinger", dt.date(1951, 7, 16), False)
    book.save()
    book = Book("To Kill a Mockingbird", "Harper Lee", dt.date(1960, 7, 11), False)
    book.save()
    book.update("isBorrowed", True)
    print(f"book_id: {book._id}")
    print(Book.fetch_object(2))
    print(Book.get_objects())

