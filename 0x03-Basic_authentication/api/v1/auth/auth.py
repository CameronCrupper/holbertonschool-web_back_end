#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar


class Auth():
    """class to define authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns boolean of if user is auth"""
        if path is None or excluded_paths is None:
            return True

        if path in excluded_paths or f"{path}/" in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """This will get flask request object"""
        if request is None or request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """This will get flask request object"""
        return None
