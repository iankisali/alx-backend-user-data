#!/usr/bin/env python3
"""Encrypting passwords and checking validity"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ perform the hashing (with hashpw)."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
