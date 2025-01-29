#!/usr/bin/env python3
"""This module is for the Session Authenication
class"""
from api.v1.auth.auth import Auth
import os
import uuid

class SessionAuth(Auth):
    """Session Auth class that inheirts
    from Auth class"""
    def __init__(self):
        super().__init__()


    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session type session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
