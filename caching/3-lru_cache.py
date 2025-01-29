#!/usr/bin/env python3
"""This is a module using Least Recently Used
algorithims"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This is the Least Recently Used Algorithims
    class."""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key: int) -> int:
        """Gets the value in the cache"""
        if key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None

    def put(self, key: int, item: int) -> None:
        """Updates the value in the value in the
        cache using Least Recently Used algorithims"""
        if key is None:
            return None
        if item is None:
            return None
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and \
                    key not in self.cache_data:
                popped = self.cache_data.popitem(last=False)
                print(f"DISCARD: {popped[0]}")
                del popped
            elif key in self.cache_data:
                self.cache_data.pop(key)

            self.cache_data[key] = item
