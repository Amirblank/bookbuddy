from typing import List
from models.book import Book
from exceptions.errors import BookNotFoundError

class BookManager:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Book:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundError(f"Book '{title}' not found in the library.")

    def list_books(self) -> List[Book]:
        return self.books