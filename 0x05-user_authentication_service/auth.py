#!/usr/bin/env python3
"""
password encrypt
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    hash password
    """
    return hashpw(password.encode('utf8'), gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Register User
        """
        try:
            consult = self._db.find_user_by(email=email)
            raise ValueError(f'<{consult.email}> already exists.')

        except NoResultFound:
            passwd: str = _hash_password(password)
            user = self._db.add_user(email, passwd)

        return user
