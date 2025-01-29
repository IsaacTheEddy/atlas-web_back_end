#!/usr/bin/env python3
"""This is my async generator"""
import asyncio
import random


async def async_generator() -> object:
    """This will yeild numbers in range of 10"""
    numbers = []
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
