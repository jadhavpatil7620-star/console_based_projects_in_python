class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter book ID: "))

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.\n")
                return

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.books.append(Book(book_id, title, author))
        print("Book added successfully.\n")

    def issue_book(self):
        book_id = int(input("Enter book ID to issue: "))

        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print("Book already issued.\n")
                else:
                    book.is_issued = True
                    print("Book issued successfully.\n")
                return

        print("Book not found.\n")
        
    def return_book(self):
        book_id=int(input("Enter book ID to return: "))
        for book in self.books:
            if book.book_id==book_id:
                if not book.is_issued:
                    print("Book is already returned.\n")
                else:
                    book.is_issued=False
                    print("Book returned successfully.\n")
                return
            print("Book is not available.\n")
        
    def search_by_id(self, search_id):
        for book in self.books:
            if book.book_id == search_id:
                print(f"Book ID: {book.book_id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Issued: {book.is_issued}\n")
                return

        print("Book not found.\n")


manager = LibraryManager()

while True:
    print("1. Add Book")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Retun book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        manager.add_book()
    elif choice == 2:
        bid = int(input("Enter book ID: "))
        manager.search_by_id(bid)
    elif choice == 3:
        manager.issue_book()
    elif choice==4:
        manager.return_book()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")