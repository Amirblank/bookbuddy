from typing import Dict, Any
from models.book import Book

class EBook(Book):
    def __init__(self, title: str, author: str, genre: str, pages: int, file_size: str) -> None:
        super().__init__(title, author, genre, pages)
        self.file_size: str = file_size

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["type"] = "EBook"
        data["file_size"] = self.file_size
        return data