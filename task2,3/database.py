from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


        
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)
    author = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    is_borrowed = db.Column(db.Boolean ,default=False )

    def __init__(self,name,author,publication_year):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        print('the object is created succussfully')

    def __repr__(self):
        return f"<Book(name={self.name})>"
    

#to interact with tha database or change anything in it
with app.app_context():
    db.create_all()

    
def add_book(book1):
        with app.app_context():
            db.session.add(book1)
            db.session.commit()

def view_books():
        with app.app_context():
            books = Book.query.all()
            
            for book in books:
                print (f"<{book.id}> Book's name: {book.name}   Author's name: {book.author}   puclication year: {book.publication_year}   status: {"borrowed" if book.is_borrowed else "available"}") 

def borrow_book(book_id):
        with app.app_context():
            
            book = Book.query.filter_by(id=book_id).first()
            if book.is_borrowed == False:
                book.is_borrowed=True
                db.session.commit()
                print (f"book {book_id} was borrowed successfully")
            else:
                print("the book is not available right now")
                choice = input("Do You want to borrow another Book (y/n): ")
                while choice.lower() not in ['y','n']:
                    choice = input("Invalid,please Enter(y/n): ")
                if choice =='y':
                    return '3'
                elif choice =='n':
                    return None
    
def return_book(book_id):
        with app.app_context():
            book = Book.query.filter_by(id=book_id).first()
            if book.is_borrowed ==True:
                book.is_borrowed=False
                db.session.commit()
                print (f"book {book_id} was returned successfully")
            else:
                print("this book is not borrowed")
                choice = input("do you want to return another book (y/n): ")
                while choice.lower() not in ['y','n']:
                    choice = input("please enter a valid answer(y/n): ")
                if choice == 'y':
                    return '4'
                else:
                     return None 
               
def delete_book(id):
        with app.app_context():

            book = Book.query.get(id)
            db.session.delete(book)
            db.session.commit()
            if Book.query.count()==0:
                return
            else:
                for new_id,book in enumerate(Book.query.all(),start=1):
                    book.id=new_id

            db.session.add(book)
            db.session.commit()
            


      





        
    