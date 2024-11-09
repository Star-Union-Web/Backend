LibraryList = []
borrowedBooks = []

class Book:
    def __init__(self, title, author, publication_year,isBorrowed):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isBorrowed = isBorrowed
    
    def borrow_book(self):
        if self.isBorrowed:
            return "The book is already borrowed."
        else:
            self.isBorrowed = True
            return "The book has been borrowed."
    
    def return_book(self):
        if not self.isBorrowed:
            return "The book is already in the library."
        else:
            self.isBorrowed = False
            return "The book has been returned."
    
    def display_book_info(self):
        return f"   Title: {self.title}\n   Author: {self.author}\n   Publication Year: {self.publication_year}\n   Borrowed: {' Yes' if self.isBorrowed else ' No'}"
    

class Library:
    def add_book(self):
        title = input('Enter the title of the book : ')
        while title == '':
            title = input('Title cannot be empty. Enter the title of the book : ')
        author = input('Enter the author of the book : ')
        while author == '':
            author = input('Author cannot be empty. Enter the author of the book : ')
        publication_year = input('Enter the publication year of the book : ')

        while True:
            try:
                publication_year = int(publication_year)
                if publication_year<1000 or publication_year>9999 :
                    print('Invalid choice. Please enter a logical year number.')
                    publication_year = input('Enter the publication year of the book : ')
                else:
                    break
            except ValueError:
                print('Invalid input. Publication year should be a number.')
                publication_year = input('Enter the publication year of the book : ')
            
        new_book = Book(title,author, publication_year, isBorrowed=False)
        LibraryList.append(new_book)
        print('Book added successfully')
    
    def view_books(self):
        if len(LibraryList):
            count = 1
            for i in LibraryList:
                print(f'{count} - \n{i.display_book_info()}')
                count += 1
        else:
            print('No books in the library')
    
    def borrow_book(self):
        Library.view_books(Book)
        if len(LibraryList):
            choice = input('Enter the number of the book you want to borrow : ')
            while True:
                try:
                    choice = int(choice)
                    if choice<1 or choice>len(LibraryList) :
                        print(f'Invalid choice. Please enter a number between 1 and {len(LibraryList)}.')
                        choice = input('Enter your choice : ')
                    break
                except:
                    print('Invalid input. Please enter a number.')
                    choice = input('Enter your choice : ')

            if LibraryList[int(choice)-1] in borrowedBooks:
                print('The book is already borrowed')
            else:
                LibraryList[int(choice)-1].borrow_book()
                borrowedBooks.append(LibraryList[int(choice)-1])
                print('The book borrowed successfully')
        else:
            pass



    def return_book(self):
        Library.view_books(Book)
        if len(LibraryList):
            choice = input('Enter the number of the book you want to return : ')
            while True:
                try:
                    choice = int(choice)
                    while choice<1 or choice>len(LibraryList) :
                        print(f'Invalid choice. Please enter a number between 1 and {len(LibraryList)}.')
                        choice = input('Enter your choice : ')
                    break
                except:
                    print('Invalid input. Please enter a number.')
            if LibraryList[int(choice)-1] in borrowedBooks:
                borrowedBooks.remove(LibraryList[int(choice)-1])
                LibraryList[int(choice)-1].return_book()
                print('Thank you for returning the book.')
            else:
                print('The book is not currently borrowed')
        else: pass
    def viewBorrowedBooks(self):
        if len(borrowedBooks):
            count = 1
            for i in borrowedBooks:
                print(f'{count} - \n{i.display_book_info()}')
                count += 1
        else:
            print('No borrowed books')


def mainMenu():
    while True:
        print('Library Management System')
        print('-------------------------')
        print('     1 - add book')
        print('     2 - view books')
        print('     3 - borrow book')
        print('     4 - return book')
        print('     5 - view borrowed books')
        print('     6 - exit')
        choice = input('Enter your choice : ')
        while True:
            try:
                choice = int(choice)
                if choice<1 or choice>6 :
                    print('Invalid choice. Please enter a number between 1 and 6.')
                    choice = input('Enter your choice : ')
                else:
                    break
            except:
                print('Invalid input. Please enter a number.')
                choice = input('Enter your choice : ')

            
        if choice == 1:
            print()
            Library.add_book(Book)
            print()
        elif choice == 2:
            print()
            Library.view_books(Book)
            print()
        elif choice == 3:
            print()
            Library.borrow_book(Book)
            print()
        elif choice == 4:
            print()
            Library.return_book(Book)
            print()
        elif choice == 5:
            print()
            Library.viewBorrowedBooks(Book)
            print()
        elif choice == 6:
            print()
            print('Thank you for using the library management system. Goodbye!')
            print()
            break
        

mainMenu()