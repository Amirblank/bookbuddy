from abc import ABC, abstractmethod
from typing import Optional

class Readable(ABC):
    @property
    @abstractmethod
    def progress(self) -> float:
        """Calculate reading progress percentage."""
        pass

    @abstractmethod
    def log_reading(self, pages: int, notes: str = "", date: Optional[str] = None) -> None:
        """Log a reading session."""
        pass