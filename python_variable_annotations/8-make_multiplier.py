#!/usr/bin/env python3
"""THis takes a float multiplier and returns a function
that muliplies by the multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier by calling a function"""
    def func(x: float) -> float:
        return x * multiplier
    return func
