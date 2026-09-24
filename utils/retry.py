import time
import functools
import logging
from typing import Callable, Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def retry(times: int = 3, delay: float = 1.0) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logging.warning(f"Attempt {attempts} failed: {e}. Retrying...")
                    time.sleep(delay)
            raise Exception(f"Function {func.__name__} failed after {times} attempts.")
        return wrapper
    return decorator