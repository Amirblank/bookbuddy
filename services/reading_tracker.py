from services.book_manager import BookManager

class ReadingTracker:
    def __init__(self, book_manager: BookManager) -> None:
        # Initialize with BookManager
        self.book_manager: BookManager = book_manager

    def log_reading(self, title: str, pages: int, notes: str = "") -> bool:
        # Log reading session for a book
        try:
            book = self.book_manager.find_book(title)
            book.log_reading(pages, notes)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False