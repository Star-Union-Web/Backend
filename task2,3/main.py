from database import Book,add_book,view_books,app,borrow_book,return_book,delete_book,db

def IsEmpty_validation(string ,variable):
    while len(string) == 0:
        print(f"the {variable} is empty  ,Enter a valid one")
        string = input(f"enter the {variable} : ")

    return string

def show_menu():
    print ('='*50)
    print('1.Add a Book ')
    print('2.View Books')
    print('3.Borrow a Book')
    print('4.Return a Book')
    print('5.Delete a book')
    print('6.Exit ')
    print ('='*50)

flag = False
available_input = ['1','2','3','4','5','6']
while True:
    print()
    
    if not flag:
        show_menu()
        choice = input("enter your choice: ")
    
    while choice not in available_input:
        print("invalid choice ,please enter a valid one")
        choice = input("enter your choice: ")

    available_dates = [str(i) for i in range(1000,2025)]
    with app.app_context():
            #count the number of books
            db_size = Book.query.count()

            # put the valid choices in a list
            available_choices = [str(n) for n in range(1,db_size+1)]

            #put the names of the books in a list
            name_list = [ i[0] for i in db.session.query(Book.name).all()]

            borrow_size=0
            return_size=0

            # calculate the number of borrowed and returned books
            for i in db.session.query(Book.is_borrowed).all():
                if i[0]:
                    borrow_size+=1
                else :
                    return_size+=1

    if choice =='1':
    
        name = input("enter the book's name: ")
        name = IsEmpty_validation(name,"Book's name")

        #validate if the book was written before or not
        while name in name_list:
            print("this book already exists")
            name = input("enter another book's name: ")
        
        author = input("enter the author's name: ")
        author = IsEmpty_validation(author ,"author's name")

        publication_year = input("enter the publication year: ")
        while publication_year not in available_dates:
            print(" the date is not correct")
            publication_year = input("enter the publication_year")
        

        book = Book(name=name ,author=author, publication_year=publication_year)
        add_book(book)
        
        

    elif choice =='2':
        if db_size==0:
            print ("the library is empty")
            continue

        view_books()


    elif choice=='3':
        if db_size==0:
            print("the list is empty, no books to be borrowed: ")
            continue

        view_books()

        if db_size==borrow_size:
            print("all the books are borrowed ,you cannot borrow any")
            continue

        book_id = input("please enter the number of the book that you want to borrow: ")

        #validate if the book's id exists in the list or not 
        while book_id not in available_choices:
                print("invalid book to borrow ,Please enter a valid one")
                book_id = input("please enter the number of the book that you want to borrow: ")

        # return_type is the answer of the user if he wants to borrow another book or not
        return_type = borrow_book(int(book_id))
        if return_type =='3':
            choice='3'
            flag = True
        else:
            flag = False

        
       
    elif choice == '4':

        if db_size==0:
            print("the list is empty, no books to be returned")
            continue
        view_books()

        if db_size==return_size:
            
            print("all the books are returned ,you cannot return any")
            continue

        book_id = input ("please enter the number of the book that you want to return: ")

        while book_id not in available_choices:
            print("invalid book to return ,Please enter a valid one")
            book_id = input("please enter the number of the book tha t you want to return: ")

        # return_type is the answer of the user if he wants to return another book or not
        return_type = return_book(int(book_id))
        if return_type == '4':
            choice = '4'
            flag =True
        else:
            flag = False
        


    elif choice =='5':
        if db_size==0:
            print("the list is empty, no books to be deleted")
            continue

        view_books()
        id = input("enter the number of book that you want to delete: ")

        while id not in available_choices:
            id = input("invalid book to be deleted enter a valid one: ")
        delete_book(int(id))

    elif choice =='6':
        print("exitting the program")
        break

    print()

    