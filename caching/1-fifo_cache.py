#!/usr/bin/python3
"""This a First in First out
class module, which inherits basecaching"""
from base_caching import BaseCaching
from typing import Dict


class FIFOCache(BaseCaching):
    """This class will use First In First Out
    algorithms to mangage the caching process"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return False

    def put(self, key:str , item: str) -> Dict[str,str]:
        """Updates the caching process using Last in
        First out"""
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
            self.queue.append(key)
        self.cache_data[key] = item
