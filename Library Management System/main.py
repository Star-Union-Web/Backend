from library import Library, Book
import json
from jsonHelper import *
from inputHandler import *

lib1 = Library()
dict_list = []

with open("books.json", "r") as f:
    
    dict_list = json.load(f)
f.close()

lib1.books = dict_list_to_obj(dict_list)

print("1.Add Book\n2.View Books\n3.Borrow Book\n4.Return Book\n5.Exit")

command = ""

while command != "5":
    if command == "1":
        title = input("Title: ")
        author = input("Author: ")
        pub_year = int(input("Publication Year: "))
        lib1.add_book(Book(title, author, pub_year))

    elif command == "2":
        lib1.list_books()

    elif command == "3":
        lib1.list_books()
        inp = input("Please Select Book ID to borrow: ")
        lib1.borrow_book(handle_idx(int(inp), len(lib1.books)))

    elif command == "4":
        lib1.list_books()
        inp =  input("Please Select Book ID to return: ")
        lib1.return_book(handle_idx(int(inp), len(lib1.books)))

    command = input(">: ")


dict_list = to_dict_list(dict_list, lib1.books)

with open("books.json", "w") as f:
    f.write("")
    f.write(json.dumps(dict_list))
f.close()