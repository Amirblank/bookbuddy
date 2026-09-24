from typing import List
from models.book import Book
from storage.json_handler import JSONHandler
from storage.pickle_handler import PickleHandler

class DataExporter:
    def export_to_json(self, books: List[Book], filename: str) -> None:
        data = [book.to_dict() for book in books]
        JSONHandler.save(data, filename)
        print(f"Data exported to '{filename}' successfully.")

    def export_to_jsonl(self, books: List[Book], filename: str) -> None:
        data = [book.to_dict() for book in books]
        JSONHandler.save_jsonlines(data, filename)
        print(f"Data exported to '{filename}' (JSON Lines) successfully.")

    def export_to_pickle(self, books: List[Book], filename: str) -> None:
        PickleHandler.save(books, filename)
        print(f"Data exported to '{filename}' successfully.")