import functools
import logging
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def log_call(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Executing: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished: {func.__name__}")
        return result
    return wrapper 