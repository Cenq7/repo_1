# Simple Library Management System

class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Year: {self.year}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        isbn = input("Enter ISBN: ")
        if isbn in self.books:
            print("Book with this ISBN already exists.")
            return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = input("Enter Year: ")
        self.books[isbn] = Book(isbn, title, author, year)
        print("Book added.")

    def delete_book(self):
        isbn = input("Enter ISBN to delete: ")
        if isbn in self.books:
            del self.books[isbn]
            print("Book deleted.")
        else:
            print("Book not found.")

    def update_book(self):
        isbn = input("Enter ISBN to update: ")
        if isbn in self.books:
            title = input("Enter new Title: ")
            author = input("Enter new Author: ")
            year = input("Enter new Year: ")
            self.books[isbn] = Book(isbn, title, author, year)
            print("Book updated.")
        else:
            print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for book in self.books.values():
                print(book)

    def book_info(self):
        isbn = input("Enter ISBN to search: ")
        if isbn in self.books:
            print(self.books[isbn])
        else:
            print("Book not found.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Update Book")
        print("4. List All Books")
        print("5. Book Info")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.delete_book()
        elif choice == "3":
            library.update_book()
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            library.book_info()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()