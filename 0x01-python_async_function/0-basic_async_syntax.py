#!/usr/bin/env python3
"""
basic async
"""


import asyncio
import time
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    pauses and waits
    """
    pause: float = random.uniform(0, max_delay)
    await asyncio.sleep(pause)
    return pause
