#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        needs documentation when you get back here
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)

        return (super(RedactingFormatter, self).format(record))


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    returns log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    takes no arguments and returns logging.Logger object
    """
    log: logging.Logger = logging.getLogger('user_data')
    log.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.setFormatter((RedactingFormatter(fields=PII_FIELDS)))
    stream_handler.formatter(formatter)

    log.addHandler(stream_handler)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a point of connection toward the database
        Return:
            A connection toward the database
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    passw = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hosting = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    medb = mysql.connector.connect(
        host=hosting,
        username=username,
        password=passw,
        database=db
    )

    return medb
