#!/usr/bin/env python3
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
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

def call_history(method: Callable) -> Callable:
    """
    This will store the history of inputs and outputs
    for a particular function

    Args:
    method (Callable): the function this wraps around

    Returns:
    Callabale: Calls the function
    """
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        This will append the inputs and outputs
        to their list respectively
        """

        self._redis.rpush(inputs, str(args))
        results = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(results))
        return results
    return wrapper


class Cache:
    """Cache class to inherit with Redis."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

def replay(method: Callable) -> None:
    """ Formats all teh data collection for display purposes

    Args:
        method (Callable): Can take any method defined
    """

    method_name = method.__qualname__
    count_key = method_name
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    count = method.__self__._redis.get(count_key)
    inputs = method.__self__._redis.lrange(inputs_key, 0, -1)
    outputs = method.__self__._redis.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {int(count)} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method_name}(*{input_str.decode('utf-8')}) ->\
            {output_str.decode('utf-8')}")
