#!/usr/bin/env python3
"""THis is a helper funcion"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This is a helper function that will
    set the current page size. """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
