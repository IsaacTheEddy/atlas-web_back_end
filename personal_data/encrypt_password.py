#!/usr/bin/env python3
"""This module is for checking and validating passwords
using the bcrypt module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a string and returns it as a password"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(bytes, salt)
    return hash_pass


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks to see if a password matches a hashed password"""
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, hashed_password)
    return result
