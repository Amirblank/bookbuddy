from typing import List, Dict, Any
from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook
from models.reading_log import ReadingLog
from storage.json_handler import JSONHandler
from storage.pickle_handler import PickleHandler

class DataImporter:
    def _create_book_from_dict(self, data: Dict[str, Any]) -> Book:
        book_type = data.get("type", "Book")
        if book_type == "EBook":
            book = EBook(data['title'], data['author'], data['genre'], data['pages'], data.get('file_size', ''))
        elif book_type == "AudioBook":
            book = AudioBook(data['title'], data['author'], data['genre'], data['pages'], data.get('duration', ''))
        else:
            book = Book.from_dict(data)

        book._Book__pages_read = data.get("pages_read", 0)
        if "reading_logs" in data:
            for log_data in data["reading_logs"]:
                log = ReadingLog(log_data["date"], log_data["pages_read"], log_data["notes"])
                book.reading_logs.append(log)
        return book

    def import_from_json(self, filename: str) -> List[Book]:
        data_list = JSONHandler.load(filename)
        return [self._create_book_from_dict(data) for data in data_list]

    def import_from_jsonl(self, filename: str) -> List[Book]:
        data_list = JSONHandler.load_jsonlines(filename)
        return [self._create_book_from_dict(data) for data in data_list]

    def import_from_pickle(self, filename: str) -> List[Book]:
        return PickleHandler.load(filename)