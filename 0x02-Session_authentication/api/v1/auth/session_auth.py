#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session Auth class with several instances"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if not user_id or type(user_id) != str:
            return
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[user_id] = session_id
        return session_id
