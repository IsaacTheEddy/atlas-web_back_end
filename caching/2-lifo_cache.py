#!/usr/bin/python3
"""This a First in Last out
class module, which inherits basecaching"""
from base_caching import BaseCaching
from typing import Dict


class LIFOCache(BaseCaching):
    """This class will use First In Last Out
    algorithms to mangage the caching process"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key: str, item: str) -> Dict[str, str]:
        """This will update the dictionary
        - if the dict is bigger than the max numbers
        it will delete the last key"""
        if key is None or item is None:
            return None
        else:
            self.queue.append(key)
            add = self.cache_data[key] = item
            if (len(self.cache_data) - 1) >= BaseCaching.MAX_ITEMS:
                if self.cache_data[key] == key:
                    self.cache_data[key] = item
                delet = self.queue.pop(-1 - 1)
                print(f"DISCARD: {delet}")
                del self.cache_data[delet]
                return self.cache_data
            else:
                return add

    def get(self, key: str) -> str:
        """This function prints the entered key"""
        if key is None:
            return None
        else:
            return self.cache_data.get(key)
