#!/usr/bin/env python3


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    wait_random: waits random amount of time
    wait_n: takes 2 ints and returns list of all delays
    Max_delay: waits max of 10 seconds
    """
    pause: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        pause.append(delay)

    return pause
