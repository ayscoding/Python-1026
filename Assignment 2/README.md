# Library Management System

This Python program implements a menu-driven library management system where users can add new books, borrow books, return books, and view the list of all available books in the library. The program ensures proper validation for inputs, including ISBN numbers and book details, and maintains the borrowing status of each book.

## Features

### 1. Add a New Book
- Allows users to add a new book to the library's inventory.
- Validates the following details:
  - **Book Name**: Ensures no invalid characters (`*`, `%`) are present.
  - **Author Name**: Allows any valid string input.
  - **Edition**: Must be a valid integer.
  - **ISBN**: Must be exactly 13 digits and pass the ISBN-13 validation algorithm.
- Prevents duplicate ISBNs from being added.

### 2. Borrow Books
- Users can borrow books by entering:
  - A **borrower's name**.
  - A **search term** to locate books:
    - A search term ending with `*` matches books that contain the term.
    - A search term ending with `%` matches books that start with the term.
    - An exact match searches for books with the exact name.
- Updates the borrowing status and assigns the borrower to the book.

### 3. Return a Book
- Users can return books by entering the ISBN of the borrowed book.
- Validates whether the book is currently borrowed.

### 4. List All Books
- Displays all books in the library along with their details:
  - Availability status (`[Available]` or `[Unavailable]`).
  - Book name, author, edition, and ISBN.
  - List of borrowers (if any).

### 5. Exit
- Exits the program after displaying the final list of books.

## Input Validations
- **ISBN Validation**:
  - Ensures the ISBN is exactly 13 digits.
  - Uses the ISBN-13 validation algorithm to check for correctness.
- **Edition Validation**:
  - Ensures the edition is a valid integer.
- **Book Name Validation**:
  - Ensures no invalid characters (`*`, `%`) are used.
- **Duplicate ISBN Check**:
  - Prevents duplicate entries of the same ISBN in the library.

## How to Use
1. Run the program.
2. Use the menu to choose one of the following options:
   - Add a new book (`1`, `a`, `A`).
   - Borrow books (`2`, `r`, `R`).
   - Return a book (`3`, `t`, `T`).
   - List all books (`4`, `l`, `L`).
   - Exit the program (`5`, `x`, `X`).
3. Follow the on-screen prompts for input.
4. Upon exiting, the final list of books is displayed.
