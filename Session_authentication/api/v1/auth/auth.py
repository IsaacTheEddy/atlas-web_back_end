#!/usr/bin/env python3
"""This is a Base Autentication module
    - Class Auth
    - Auth Methods"""


from flask import request
from typing import List


class Auth():
    """The auuthentication class.
    Methods
    - require_auth - Returns which paths require authorization
    - authorization_header - Returns the auth header
    - current_user - Returns current user
    """
    def __init__(self):
        """Iniitalizer method"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns whether the path requires authentication
        based on excluded paths."""
        if path and excluded_paths:
            if path.endswith('/') is False:
                pathcorrect = path + '/'
                if pathcorrect in excluded_paths:
                    return False
                else:
                    return True
            if path in excluded_paths:
                return False
            else:
                return True
        if path is None or not excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Returns None with flask request object"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> str:
        """Returns None with the flask request object"""
        return None
