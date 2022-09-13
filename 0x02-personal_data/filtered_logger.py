#!/usr/bin/env python3
"""
Regex-ing
"""

from typing import List
from re import sub


def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """
    returns log message obfuscated
    """
    for field in fields:
        message = sub(f'{field}=.+?{separator}', f'{field}={redaction}{separator}', message)
    return message
