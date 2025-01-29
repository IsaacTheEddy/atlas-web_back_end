#!/usr/bin/env python3
"""This will get the page and the next page and previous page."""
import csv
import math
from typing import List, Dict
pg = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the page and returns it with page info"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        result = self.dataset()
        start_index, end_index = pg(page, page_size)
        if start_index >= len(result):
            return []
        return result[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, str]:
        """This will return key-value pairs of pages and page sizes"""
        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_pag = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_pag,
            "total_pages": total_pages
            }
