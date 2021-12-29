#!/usr/bin/env python3

import sys

word_length = len(sys.argv[1])
if word_length % 2 == 0:
    print(sys.argv[1][word_length // 2:])

else:
    print(sys.argv[1][0] + sys.argv[1][-1])
