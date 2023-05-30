#!/usr/bin/env python3
"""Authenticatin file"""
from flask import request
from typing import List, TypeVar
from tabnanny import check
User = TypeVar('User')


class Auth:
    """class managing API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        if request is None:
            return None
        return request.headers.get("Authorixation")

    def current_user(self, request=None) -> TypeVar('User'):
        """returns none"""
        return None