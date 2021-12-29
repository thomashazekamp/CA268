#!/usr/bin/env python3

import sys

text = sys.argv[1]

n = 0
i = 2
while n < (len(text) - 1):
    print(text[n:i])
    i = i + 1
    n = n + 1