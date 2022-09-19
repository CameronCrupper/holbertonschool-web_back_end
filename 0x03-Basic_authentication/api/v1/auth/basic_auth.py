#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64 import b64decode
import re
from models.user import User


class BasicAuth(Auth):
    """class to define authorization"""
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        base64 decode
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')

        except Exception:
            return None
