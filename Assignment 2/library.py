# ISBN validation process phase 2
def isbn_validate(isbn):
    if len(isbn) != 13 or not isbn.isdigit():
        return False
    
    factors = [1, 3] * 6 
    factors.append(1)
    total = 0
    for digit, factor in zip(isbn, factors):
        total += int(digit) * factor

    
    return total % 10 == 0

# The function call for "1,a,A", Adding new book
def new_book(allBooks):
    while True:
        book_name = input("Book name> ")
        if '*' in book_name or '%' in book_name:
            print("Invalid character '*' or '%' found in the book name. Please try again.")
        else:
            break

    author_name = input("Author name> ")

    while True:
        edition = input("Edition> ")
        if not edition.isdigit():
            print("Invalid input for edition. Please enter a valid integer.")
        else:
            break
    
    # ISBN validation process phase 1
    while True:
        isbn = input("ISBN> ")
        if len(isbn) != 13 or not isbn.isdigit():
            print("Invalid ISBN. Should be 13 Digits. Please Try Again")
        else:
            if not isbn_validate(isbn):
                print("Invalid ISBN. This book entry is skipped.")
                return
            if isbn in [book[0] for book in allBooks]:
                print("ISBN already exists. Book entry is skipped.")
                return
            break

    new_book = [isbn, book_name, author_name, int(edition), []]

    # Adds a new book to allBooks
    allBooks.append(new_book)       

    print("A new book is added successfully.")

# The function call for "2,r,R", Borrowing a book
def borrowed_books(allBooks, borrowedISBNs):
    borrower_name = input("Enter the name of the borrower: ")

    search_term = input("Enter the search term: ")

    borrow_count = 0

    for book in allBooks:
        if search_term.endswith('*'):
            if search_term.lower().strip('*') in book[1].lower():
                book[4].append(borrower_name)
                borrowedISBNs.append(book[0])
                borrow_count += 1

        elif search_term.endswith('%'):
            if book[1].lower().startswith(search_term.lower().strip('%')):
                book[4].append(borrower_name)
                borrowedISBNs.append(book[0])
                borrow_count += 1
                
        else:
            if search_term.lower() == book[1].lower():
                book[4].append(borrower_name)
                borrowedISBNs.append(book[0])
                borrow_count += 1

    if borrow_count == 0:
        print("No books were found.")

    return allBooks, borrowedISBNs

# The fun call for "3,t,T", to return a book
def book_return(allBooks, borrowedISBNs):
    isbn_return = input("Enter the ISBN of the book to return: ")

    if isbn_return in borrowedISBNs:
        borrowedISBNs.remove(isbn_return)
        print("Book returned successfully.")
    else:
        print("No book is found!")

# The function call for "4,l,L", lists all books
def list_all_books(allBooks):
    if not allBooks:
        print("No books were found.")
        return

    for book in allBooks:
        print('-'*13)
        if not book[4]:
            print("[Available]")
        else:
            print("[Unavailable]")
        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")
    print('-'*13)

# Menu
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')


def start():
    # Initial books, authors, borrowers
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    borrowedISBNs = []
    while True:
        printMenu()
        choice = input("Your selection> ")      # Prompts user to enter a vlaue

        # Choose a function based on user input

        if choice in ['1', 'a', 'A']:
            new_book(allBooks)
        elif choice in ['2', 'r', 'R']:
            allBooks, borrowedISBNs = borrowed_books(allBooks, borrowedISBNs)
        elif choice in ['3', 't', 'T']:
            book_return(allBooks, borrowedISBNs)
        elif choice in ['4', 'l', 'L']:
            list_all_books(allBooks)
        
        # The function call for "5,x,X" Exit
        elif choice in ['5', 'x', 'X']:
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            list_all_books(allBooks)
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            break
        else:
            print("Wrong selection! Please select a valid option.")


start()
