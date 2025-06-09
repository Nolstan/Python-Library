# Library Management System

A simple command-line library management system written in Python, allowing both admin and student users to manage and interact with books in a library.

## Features

### User Types
- **Admin**: Has full control over the system
- **Student**: Can borrow books and view available books

### Admin Functions
- Add new books to the library
- Update book information (name or ISBN)
- List all books in the library
- Remove student accounts
- Delete books from the library
- View all borrowed books
- View all available books
- Record returned books
- Search for books
- View total count of books

### Default Admin Credentials
- Admin ID: `someword` (hardcoded in the system)
- You'll need to create an admin account first using this ID
  
### Student Functions
- Borrow available books
- Search for books
- View available books
- View borrowed books
- Change password (placeholder - not fully implemented)

## How to Use

### Prerequisites
- Python 3.x
- No additional libraries required (uses built-in `csv` and `os` modules)

### Running the Program
1. Clone or download the repository
2. Navigate to the project directory
3. Run the script:
