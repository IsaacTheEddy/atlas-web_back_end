#!/usr/bin/env python3
"""This one shows how to use the optional type"""
from typing import List, Optional, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns data into a tuple """
    return (k, v * v)
