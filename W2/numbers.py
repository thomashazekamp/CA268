#!/usr/bin/env python3

def sum_to_k(list, k):

    i = 0
    j = len(list) - 1
    while i < j:
        first =  list[i]
        second = list[j]
        if (first + second) == k:
            return True
        elif (first + second) < k:
            i += 1
        elif (first + second) > k:
            j -= 1
    return False
