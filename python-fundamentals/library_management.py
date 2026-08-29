import os
import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self, filepath="library.json"):
        self.books = {}  # key = ISBN, value = Book object
        self.filepath = filepath
        self.load_books()

    def add_book(self, title, author, isbn):
        if isbn in self.books:
            print("A book with this ISBN already exists.")
        else:
            self.books[isbn] = Book(title, author, isbn)
            print(f"Book '{title}' added.")

    def remove_book(self, isbn):
        if isbn in self.books:
            removed = self.books.pop(isbn)
            print(f"Book '{removed.title}' removed.")
        else:
            print("No book found with that ISBN.")

    def search_books(self, query):
        query = query.lower()
        found = [book for book in self.books.values()
                 if query in book.title.lower() or query in book.author.lower()]
        if found:
            print("\nSearch Results:")
            for book in found:
                print(book)
        else:
            print("No books found for the search query.")

    def view_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print("\n--- Library Collection ---")
        for book in self.books.values():
            print(book)

    def save_books(self):
        with open(self.filepath, "w") as f:
            json.dump({isbn: book.to_dict() for isbn, book in self.books.items()}, f, indent=4)
        print("Library saved to file.")

    def load_books(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                data = json.load(f)
                for isbn, info in data.items():
                    self.books[isbn] = Book(info["title"], info["author"], isbn)
            print("Library loaded from file.")
        else:
            print("No existing library file found. Starting fresh.")

def main():
    library = Library()

    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. View All Books")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == "3":
            query = input("Search by title or author: ")
            library.search_books(query)
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            library.save_books()
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
