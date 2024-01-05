#!/usr/bin/python3
"""
Defines locked class.
"""


class LockedClass:
    """
    Prevent user from instantiating new LockedClass attributes
    for only the attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
