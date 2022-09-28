#!/usr/bin/env python3
"""
password encrypt
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """
    hash password
    """
    return hashpw(password.encode('utf8'), gensalt())


def _generate_uuid() -> str:
    """
    Generate uuid returns uuid in string
    """
    UUID = uuid4()

    return str(UUID)


class Auth:
    """
    Auth class to interact with the authentication database.
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

    def valid_login(self, email: str, password: str) -> bool:
        """
        validating credentials
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if checkpw(password.encode('utf-8'), user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """
        gets sessions ID
        """
        try:
            user = self._db.find_user_by(email=email)
            sess_id = _generate_uuid()
            self._db.update_user((user.id), session_id=sess_id)

            return sess_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        finds a user by session ID
        """
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)

            return user
        except (NoResultFound, InvalidRequestError):
            return None

    def destroy_session(self, user_id: str) -> None:
        """
        updates user ID to None
        """
        try:
            self._db.update_user(user_id, session_id=None)

            return None
        except ValueError:
            return None

def get_reset_password_token(self, email: str) -> str:
        """
        fins corresponding email and generates uuid
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        user.reset_token = str(uuid4())
        return user.reset_token

