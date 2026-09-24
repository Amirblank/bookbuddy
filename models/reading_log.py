from typing import Dict, Any

class ReadingLog:
    def __init__(self, date: str, pages_read: int, notes: str = "") -> None:
        # Initialize reading log
        self.date: str = date
        self.pages_read: int = pages_read
        self.notes: str = notes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "date": self.date,
            "pages_read": self.pages_read,
            "notes": self.notes
        }