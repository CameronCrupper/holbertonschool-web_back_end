#!/usr/bin/env python3
"""
password encrypt
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    hash password
    """
    return hashpw(password.encode('utf8'), gensalt())
