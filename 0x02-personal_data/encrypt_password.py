#!/usr/bin/env python3
"""
Encrypting Passwords
"""


import bcrypt


def hash_password(password: str = '') -> bytes:
    """
    expects one string arg name password and
    returns a salted, hashed password, which
    is a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
