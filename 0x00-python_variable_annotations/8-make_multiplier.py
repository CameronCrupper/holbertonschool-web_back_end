#!/usr/bin/env python3

"""
callable function
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    args: multiplier: factor

    return: multiplication in float
    """
    def x(f: float) -> float:
        """
        get second argument like JS
        """
        return float(f * multiplier)

    return x
