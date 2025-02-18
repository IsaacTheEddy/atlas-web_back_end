#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import redis.cache
import redis.client


class Cache:
    """Cache class to inherit with Redis."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get(self, key: str, fn: Callable) -> str:
        """This will get whatever is pulled from redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data


    def get_str(self, key: str) -> str:
        string = string.decode('utf-8')
        return self.get(key, string)

    def get_int(self, key: str) -> str:
        integar = integar.decode('utf-8')
        return self.get(int(key, integar))
