from typing import Dict, Any
from models.book import Book

class AudioBook(Book):
    def __init__(self, title: str, author: str, genre: str, pages: int, duration: str) -> None:
        super().__init__(title, author, genre, pages)
        self.duration: str = duration

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["type"] = "AudioBook"
        data["duration"] = self.duration
        return data