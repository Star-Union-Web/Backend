# 📚 Library Management System CLI
## 📖 Description
Library Management System CLI is a command-line application designed for efficient management of a library's book collection.

Users can add, view, borrow, and return books, with all data stored in a SQLite database.

The application offers a straightforward interface for managing books and ensures data persistence through robust database operations.

## 🚀 Running the Application
To run the Library Management System CLI, ensure that all Python files (main.py, library.py, ORM.py, and validation.py) are in the same directory.

## 🛠️ Creating the Database
You can create the SQLite database by either of the following methods:

### Run library.py:
This will create the SQLite database if it does not already exist and migrate Book class.

```bash
python library.py
```

### Run main.py:
This will start the library management system directly and also create the database if it does not exist.

```bash
python main.py
```

## ⚠️ Note
If you have an existing database file with your books, place the database file in the same directory as the Python files. This ensures the application can access your existing data.


## 🛢️ Database Schema
Books are stored in a SQLite database in the Book table with the following schema:

* **`title (TEXT):`** The title of the book.
* **`author (TEXT):`** The author of the book.
* **`publication_year (DATE):`** The publication year of the book.
* **`isBorrowed (BOOLEAN):`** The status of whether the book is borrowed or not.
  
## 📂 File Descriptions
### main.py
The main entry point for the Library Management System CLI. It initializes the ORM and runs the user interface for managing the library.

### library.py
Contains the Book and Library classes. The Book class represents a book in the library, and the Library class manages a collection of books.

### ORM.py
Handles the database operations for the Library Management System. It includes methods for creating tables, inserting records, and fetching records from the database.

### validation.py
Provides utility functions for validating user input, such as dates and choices.

## 🛠️ Usage
Add a Book: Allows the user to add a new book to the library.
View All Books: Displays all books in the library.
View Borrowed Books: Displays all borrowed books.
Borrow a Book: Allows the user to borrow a book from the library.
Return a Book: Allows the user to return a borrowed book.
Exit: Exits the application.
## 🛠️ Example Commands
To add a book

```bash
python main.py add_book
```
To view all books

```bash
python main.py view_books
```
To borrow a book

```bash
python main.py borrow_book
```
To return a book

```bash
python main.py return_book
```

## ⚠️ Configuration Note
Ensure that the config.json file is present in the same directory as the Python files. This file should contain the database configuration details.

