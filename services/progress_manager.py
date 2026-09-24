from typing import List, Dict, Any
from models.book import Book

class ProgressManager:
    @staticmethod
    def get_reading_summary(books: List[Book]) -> List[Dict[str, Any]]:
        summary = []
        for book in books:
            summary.append({
                "title": book.title,
                "pages_read": book.pages_read,
                "total_pages": book.pages,
                "progress_percent": book.progress
            })
        return summary