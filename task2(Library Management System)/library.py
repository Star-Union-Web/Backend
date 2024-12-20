class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def borrow_book(self, id):
        if self.books[id].is_borrowed == False:
            self.books[id].is_borrowed = True
        else:
            print("Sorry, This book Is unavailable.")

    def return_book(self, id):
        self.books[id].is_borrowed = False

    
    def list_books(self):
        print("-------------------------------------------------------")
        for i in range(len(self.books)):
            print(f"{i}.: Title: {self.books[i].title}")
            print(f"Author: {self.books[i].author}")
            print(f"Publication Year: {self.books[i].pub_year}")

            if self.books[i].is_borrowed == False:
                print("Availability: Available")

            else:
                print("Availability: Unavailable")

            print("-------------------------------------------------------")


class Book:
    def __init__(self, title: str, author: str, pub_year: int, is_borrowed: bool = False):
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.is_borrowed = is_borrowed


    
    
   