# Blog Project

This project is a simple blog application built with Django. It includes two main apps: **Users** and **Posts**.

## Features

### Users App
- **User Registration**: Allows users to sign up with a username, email, and password.
- **User Login**: Existing users can log in using their username and password.
- **User Logout**: Users can log out of their accounts.
- **User Profile**: Authenticated users can view their profile, which shows their username and email.

### Posts App
- **Post Management**: Authenticated users can create, edit, and delete blog posts.
- **Comments**: Authenticated users can post comments on published posts, and they can edit or delete their comments.
- **Permissions**: Only the author of a post or comment can edit or delete it.

## Directory Structure
- `Users/`: Manages user authentication (register, login, logout, profile).
- `Posts/`: Manages blog posts and comments (create, edit, delete).

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <project_folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser to manage the app (optional):
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the app in your browser at: `http://127.0.0.1:8000/`.

## URL Patterns

### Users App
- `/register/`: Register a new user.
- `/login/`: Login for existing users.
- `/logout/`: Logout the current user.
- `/profile/`: View the logged-in user's profile page.

### Posts App
- `posts/`: Display all posts.
- `posts/create/`: Create a new post.
- `posts/edit/<post_id>/`: Edit an existing post.
- `posts/delete/<post_id>/`: Delete a post.
- `posts/comments/<post_id>/`: View and add comments for a post.
- `posts/comments/delete/<comment_id>/`: Delete a comment.
- `posts/comments/edit/<comment_id>/`: Edit a comment.

## Requirements
- Python 3.12x
- requirements.txt 



