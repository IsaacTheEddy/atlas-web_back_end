#!/usr/bin/env python3
"""This module is for the Session Authenication
class"""
from api.v1.auth.auth import Auth
import os


class SessionAuth(Auth):
    """Session Auth class that inheirts
    from Auth class"""
    def __init__(self):
        super().__init__()
        pass
