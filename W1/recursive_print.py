#!/usr/bin/env python3

def rprint(a, b):
    if a == b or a > b:
        return
    else:
        print(a)
        rprint(a + 1, b)

# rprint(6, 12)