#!/usr/bin/env python3

import sys

def get_counts_dict(words_list):

    len_dict = {}

    for word in words_list:
        if len(word) not in len_dict:
            len_dict[len(word)] = 1
        else:
            len_dict[len(word)] += 1
    
    return len_dict

def main():
    # read the list of words from stdin
    line = sys.stdin.readline()
    line = line.strip()
    words = line.split()

    # call the student's function
    counts = get_counts_dict(words)
    print(type(counts))

    lengths = counts.keys()
    for length in sorted(lengths):
        print(str(length) + ": " + str(counts[length]))

if __name__ == '__main__':
    main()
