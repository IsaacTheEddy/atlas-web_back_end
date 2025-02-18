#!/usr/bin/env python3
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> callable:
    """
    Will keep track of how many calls are made to
    the cache class

    Args:
    method (Callable): the wrapper that keeps count

    Return:
    Callable: Calls the function over and over again.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):

        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class to inherit with Redis."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly genereated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: They key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None
                ) -> Optional[Union[str, int]]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
        key (str) the key name for Redis
        fn Optional[Callable[[bytes], Union[str, int]]] an optional function to be called
        if the value passed isnt a string
        Returns:
        None

        """
        value = self._redis.get(key)

        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value


    def get_str(self, key: str) -> str:
        """
        Gets the String value from Redis

        Args:
        key (str) the name of the key

        Returns:
        str: the string representation of the key: value
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
            """
        Gets the Int value from Redis

        Args:
        key (str) the name of the key

        Returns:
        int: the string representation of the key: value
        """
            return self.get(key, lambda x: int(x))


