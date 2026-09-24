import pickle
from typing import Any
from utils.context import FileHandler
from utils.decorators import log_call
from utils.retry import retry

class PickleHandler:
    @staticmethod
    @log_call
    @retry(times=3)
    def save(data: Any, filename: str) -> None:
        with FileHandler(filename, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    @log_call
    @retry(times=3)
    def load(filename: str) -> Any:
        with FileHandler(filename, 'rb') as f:
            return pickle.load(f)