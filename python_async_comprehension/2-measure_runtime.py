#!/usr/bin/env python3
"""This is a function to run 4 parellel
comprehensions"""

import asyncio
import time

ac = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """This will start my count timer and then start my async
    comprehension function. This will send it into a list."""
    parellel = [ac(), ac(), ac(), ac()]
    start = time.perf_counter()
    await asyncio.gather(*parellel)
    elapsed = time.perf_counter() - start
    return elapsed
