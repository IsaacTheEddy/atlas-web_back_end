#!/usr/bin/env python3
"""This module is duck typing, QUACK"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """List comprehends for lst"""
    return [(i, len(i)) for i in lst]
