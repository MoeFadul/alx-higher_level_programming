#!/usr/bin/python3
"""
Defines a text file-reading function
"""

def read_file(filename=""):
    """"prints whats in UTF8 to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
