#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class to define authorization"""
