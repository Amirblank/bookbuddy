from datetime import datetime
from typing import List, Dict, Any, Optional, Type, TypeVar
from models.readable import Readable
from models.reading_log import ReadingLog

T = TypeVar('T', bound='Book')

class Book(Readable):
    def __init__(self, title: str, author: str, genre: str, pages: int) -> None:
        # Initialize book attributes
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.pages: int = pages
        self.date_added: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__pages_read: int = 0
        self.reading_logs: List[ReadingLog] = []

    def log_reading(self, pages: int, notes: str = "", date: Optional[str] = None) -> None:
        # Update pages read

        if pages < 0:
            raise ValueError("Pages read cannot be negative.")
        if self.__pages_read + pages > self.pages:
            raise ValueError("Total pages read cannot exceed book pages.")

        self.__pages_read += pages
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        log_entry = ReadingLog(date, pages, notes)
        self.reading_logs.append(log_entry)

    @property
    def progress(self) -> float:
        # Calculate reading progress
        if self.pages == 0:
            return 0.0
        return (self.__pages_read / self.pages) * 100

    @property
    def pages_read(self) -> int:
        # Create a Book instance from dictionary
        return self.__pages_read

    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        if not cls.validate_data(data):
            raise ValueError("Invalid data for Book")
        book = cls(data['title'], data['author'], data['genre'], data['pages'])
        book.date_added = data.get('date_added', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        book._Book__pages_read = data.get('pages_read', 0)
        return book

    @staticmethod
    def validate_data(data: Dict[str, Any]) -> bool:
        # Validate book data
        required_keys = ['title', 'author', 'genre', 'pages']
        for key in required_keys:
            if key not in data:
                return False
        if not isinstance(data['pages'], int) or data['pages'] <= 0:
            return False
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages,
            "date_added": self.date_added,
            "pages_read": self.__pages_read,
            "reading_logs": [log.to_dict() for log in self.reading_logs]
        }