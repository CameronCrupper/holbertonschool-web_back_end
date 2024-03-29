#!/usr/bin/env python3
"""
Mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    takes list of ints and floats and returns sum as float
    """
    return sum(mxd_list)
