#!/usr/bin/env python3
""" This module is Deletion-resilient hypermedia
pagination"""

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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns key-value pairs for items in a database by page number
        and page size. And remembers the postion in case of deletion"""

        # Make sure that index is an int < the dataset length
        assert isinstance(index, int) and index < len(self.dataset()), \
            "Invalid index"

        start_index = index
        end_index = min(start_index + page_size, len(self.dataset()))
        current_page = self.dataset()[start_index:end_index]

        # Calculate next_index
        next_index = end_index

        # Calculate total_items
        total_items = len(self.dataset())

        data_dict = {
            "index": index,
            "page_size": page_size,
            "next_index": next_index,
            "data": current_page,
        }

        return data_dict
