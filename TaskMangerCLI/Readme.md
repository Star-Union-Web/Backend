🗂️ Task Manager CLI
📖 Description
Task Manager CLI is a command-line application designed for efficient task management. Users can create, view, update, and delete tasks, with all data stored in a SQLite database. The application offers a straightforward interface for managing tasks and ensures data persistence through robust database operations.

🚀 Running the Application
To run the Task Manager CLI, ensure that all three Python files (CLI.py, database.py, and validation.py) are in the same directory.

🛠️ Creating the Database
You can create the SQLite database by either of the following methods:

Run database.py:
This will create the SQLite database if it does not already exist.

bash
Copy code
python database.py
Run CLI.py:
This will start the task manager directly and also create the database if it does not exist.

bash
Copy code
python CLI.py
⚠️ Note
If you have an existing database file with your tasks, place the database file in the same directory as the Python files. This ensures the application can access your existing data.

🛢️ Database Schema
Tasks are stored in a SQLite database in the task table with the following schema:

⏺ title (TEXT, UNIQUE): The title of the task.
⏺ description (TEXT): A description of the task.
⏺ due_date (DATE): The due date of the task.
⏺ priority (INTEGER): The priority level of the task.