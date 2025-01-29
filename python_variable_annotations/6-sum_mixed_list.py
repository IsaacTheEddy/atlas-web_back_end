#!/usr/bin/env python3
"""This modules returns a single float for a mixed list"""
from typing import List, Union


def sum_mixed_list(mxd: List[Union[int, float]]) -> float:
    """Returns a float from a mixed list"""
    return sum(mxd)
