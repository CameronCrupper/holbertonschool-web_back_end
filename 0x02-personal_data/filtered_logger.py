#!/usr/bin/env python3
"""
Regex-ing
"""

from typing import List
from re import sub
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))

def filter_datum(fields: List, redaction: str, message: str, separator: str):
    """
    returns log message obfuscated
    """
    for field in fields:
        message = sub(f'{field}=.+?{separator}', f'{field}={redaction}{separator}', message)
    return message

def get_logger() -> logging.Logger:
    """
    takes no arguments and returns logging.Logger object
    """
    log: logging.Logger = logging.getLogger('user_data')
    log.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter((RedactingFormatter(fields=PII_FIELDS)))
    stream_handler.formatter(formatter)

    log.addHandler(stream_handler)

    return log
