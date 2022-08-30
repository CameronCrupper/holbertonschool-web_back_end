#!/usr/bin/env python3
"""
task that takes int and returns asyncio.task
"""


import asyncio
import time
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10):
    """
    max_delay is 10
    returns task thats been created
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
