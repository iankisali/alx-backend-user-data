#!/usr/bin/env python3
"""Filtered logger file"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: string rep character separating all fields in log line (message)
    """
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message
