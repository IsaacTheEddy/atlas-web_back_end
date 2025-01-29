#!/usr/bin/env python3
"""Will display a asynchronous function max delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Uses async to find to delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
