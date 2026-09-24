import json
from typing import List, Dict, Any
from utils.context import FileHandler
from utils.decorators import log_call
from utils.retry import retry

class JSONHandler:
    @staticmethod
    @log_call
    @retry(times=3)
    def save(data: List[Dict[str, Any]], filename: str) -> None:
        with FileHandler(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    @log_call
    @retry(times=3)
    def load(filename: str) -> List[Dict[str, Any]]:
        with FileHandler(filename, 'r') as f:
            return json.load(f)

    @staticmethod
    @log_call
    @retry(times=3)
    def save_jsonlines(data: List[Dict[str, Any]], filename: str) -> None:
        with FileHandler(filename, 'w') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')

    @staticmethod
    @log_call
    @retry(times=3)
    def load_jsonlines(filename: str) -> List[Dict[str, Any]]:
        data = []
        with FileHandler(filename, 'r') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
        return data