#!/usr/bin/env python3
"""
measures runtime
"""


import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    measures total execution time and returns float
    """
    first = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first
    total = elapsed / n
    return total
