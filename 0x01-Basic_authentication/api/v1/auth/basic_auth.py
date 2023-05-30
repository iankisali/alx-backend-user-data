#!/usr/bin/env python3
"""Basic auth modile"""
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns decoded val of Base64 string base64_authorization_header"""
        b64_auth_header = base64_authorization_header
        if b64_auth_header and isinstance(b64_auth_header, str):
            try:
                encode = b64_auth_header.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        decode_64 = decoded_base64_authorization_header
        if (decode_64 and isinstance(decode_64, str) and ":" in decode_64):
            result = decode_64.split(":", 1)
            return (result[0], result[1])
        return (None, None)
