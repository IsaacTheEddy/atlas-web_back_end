import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[bytes, str, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        if isinstance(data, bytes):
            try:
                return fn(int(data)) if callable(fn) else int(data)
            except ValueError:
                return fn(data) if callable(fn) else data
        return fn(data) if callable(fn) else data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key)

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key)
