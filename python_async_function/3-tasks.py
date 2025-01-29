#!/usr/bin/env python3
"""Takes an integer for max delay and returns asynchio.Task"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Made a asyncio task that does a asyncio function
    i just typed it in and it worked, I love python and i
    blow my self away"""
    return asyncio.create_task(wait_random(max_delay))
