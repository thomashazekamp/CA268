#!/usr/bin/env python3

def maximum(list):
    # base case
    if len(list) == 1:
        return print(list[0])
    else:
        if list[0] > list[1]:
            del list[1]
            maximum(list)
        elif list[0] == list[1]:
            print(list[0])
            del list[1]
            maximum(list)
        else:
            del list[0]
            maximum(list)

maximum([2, 4, 6])