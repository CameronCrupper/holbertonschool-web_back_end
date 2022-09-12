#!/usr/bin/env python3
"""
Simple Helper Function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns tuple of size two that contains a start index and
    an end index
    """
    final_size: int = page * page_size
    start_size: int = final_size - page_size
    return (start_size, final_size)
