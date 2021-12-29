#!/usr/bin/env python3

import sys

# Lab task Number 1, get_odd_list
def get_odd_list():

    odd_list = []
    for number in sys.stdin:
        number = int(number.strip())
        if number == -1:
            return odd_list
        if number % 2 != 0:
            odd_list.append(number)
    return odd_list

# Lab task Number 2, get_evenodd_list
def get_evenodd_list():

    odd_list = []
    even_list = []
    for number in sys.stdin:
        number = int(number.strip())
        if number == -1:
            return odd_list, even_list
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return odd_list, even_list

# Lab task Number 3, get_sliced_lists
def get_sliced_lists(list):

    list_nlast = list[0:-1]
    list_nfirstlast = list[1:-1]
    reverse_list = list[::-1]
    return list_nlast, list_nfirstlast, reverse_list

def get_counts(words):

    counts_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in words:
        len_pos = len(i)
        counts_list[len_pos] += 1
    return counts_list


def main():
        # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function and ...
    counts = get_counts(words)
    # ... print the result
    for length in range(10):
        print(str(length) + ": " + str(counts[length]))

if __name__ == '__main__':
    main()
