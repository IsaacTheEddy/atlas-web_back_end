#!/usr/bin/env python3
"""This module is for my basic auth class"""
from api.v1.auth.auth import Auth
import base64
from typing import List, Tuple , TypeVar
from api.v1.views.users import User


class BasicAuth(Auth):
    """This is a basic authenication
    class that inherits from my Auth class"""
    def __init__(self):
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base4 part of the Authoruzation
        Header"""
        if authorization_header is None:
            return None
        str_auth = str(authorization_header)
        if str_auth.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes a header thats given to it in base64"""
        if base64_authorization_header is None:
            return None
        str_auth = base64_authorization_header
        try:
            decoded_auth = base64.b64decode(str_auth)
            utf = decoded_auth.decode('utf-8')
            return utf
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[(str, str)]:
        """Returns a users email and password from Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        str_decoded_auth  = str(decoded_base64_authorization_header)
        if str_decoded_auth.find(":") < 1:
            return (None, None)
        else:
            n_e = str_decoded_auth.split(":")
            return (n_e)

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        """Returns a User Instance based on their emial and password"""
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        user  = User.search({"email": user_email})
        if user is None:
            return None
        for users in user:
            if users.is_valid_password(user_pwd):
                return users

    def current_user(self, request=None):
        """This overloads Auth and retrieves the User instance"""
        if request is None:
            return None
        authorization_header = request.headers.get('Authorization')
        if authorization_header is None:
            return None
        base64_auth_header = self.extract_base64_authorization_header(authorization_header)
        if base64_auth_header is None:
            return None
        decoded_auth = self.decode_base64_authorization_header(base64_auth_header)
        if decoded_auth is None:
            return None
        user_email, user_pwd = self.extract_user_credentials(decoded_auth)
        if user_email is None or user_pwd is None:
            return None
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
