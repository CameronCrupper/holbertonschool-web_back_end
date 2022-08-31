#!/usr/bin/env python3
"""
Async Generator
"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times and each time waits 1 second
    then yeilds random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
