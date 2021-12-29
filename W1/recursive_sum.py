#!/usr/bin/env python3

def sumto(a, b):
    # base case
    if a == b:
        return b
    else:
        return b + sumto(a, b - 1)
