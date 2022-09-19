#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """class to define authorization"""

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        basic user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' in decoded_base64_authorization_header:
            return decoded_base64_authorization_header.split(':')
        else:
            return None, None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
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

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method"""
        auth = request.headers.get('Authorization')
        header = self.extract_base64_authorization_header(auth)
        decoded_header = self.decode_base64_authorization_header(header)
        email, passwd = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(email, passwd)
