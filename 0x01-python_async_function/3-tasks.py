#!/usr/bin/env python3
"""
task that takes int and returns asyncio.task
"""


import asyncio
import time
from typing import List

wait_n = __import__('2-measure_runtime').wait_n


def task_wait_random(max_delay: int = 10):
    """
    max_delay is 10
    returns task thats been created
    """
    task = asyncio.create_task(wait_n(max_delay))
    return task
