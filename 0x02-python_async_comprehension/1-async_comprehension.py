#!/usr/bin/env python3
"""
async comprehensions
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random num from async_gen then returns 10 random nums
    """
    return ([i async for i in async_generator()])
