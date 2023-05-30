#!/usr/bin/env python3
"""Basic auth modile"""
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Class BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns Base64 part of Authorization header for Basic Auth"""
        if (authorization_header is None or not
                isinstance(authorization_header, str)
                or not authorization_header.startswith("Basic")):
            return None

        return authorization_header[6:]
