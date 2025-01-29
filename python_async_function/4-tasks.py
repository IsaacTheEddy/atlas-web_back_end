#!/usr/bin/env python3
"""Will display a asynchronous function max delay and max ns"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes an empty list for results so object properties arent stored
    creates async tasks with functions in a list the 'n' amount of times requested
    and uses the as completed generator to collect as completed and store
     in a list. """
    results = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
