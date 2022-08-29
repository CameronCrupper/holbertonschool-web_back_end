#!/usr/bin/env python3

from typing import Tuple, Union

def to_kv(k: str, v: Union[float, int]) -> Tuple[float, str]:

    return (k, v * v)
