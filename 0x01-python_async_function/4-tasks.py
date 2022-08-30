#!/usr/bin/env python3
"""
calling task_wait_random
"""


import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    takes code from wait_n and turns it into task_wait_n
    """
    pauses: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        pause = await task
        pauses.append(pause)

    return pauses
