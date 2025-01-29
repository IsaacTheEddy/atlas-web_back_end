#!/usr/bin/python3
"""This will inheirt from base_caching.
It will add cached items to a dictionary."""
from base_caching import BaseCaching
from typing import Dict


class BasicCache(BaseCaching):
    """This class is inherited from base_caching,
    Its a basic cache so all it will do is update
    the cache dictionary and return to me data representing
    the caches state"""
    def __init__(self):
        super().__init__()

    def put(self, key: str, item: str) -> Dict[str, str]:
        """This function updates the dicitonary
        with a key, item value"""
        if key is None or item is None:
            return None
        else:
            add = self.cache_data[key] = item
            return add

    def get(self, key: str) -> str:
        """This function prints the entered key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
