# library_management.py

class Book:
    """Represents a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book instances."""
    
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Adds a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # Optionally: print or log a message if not found or already checked out

    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # Optionally: print or log a message if not found or not checked out

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)