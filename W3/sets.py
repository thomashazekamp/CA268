#!/usr/bin/env python3

import sys

# Lab task Number 3 of sets.py, unique_list
def unique_list(lst):

    return list(set(lst))

# Lab task Number 2 of sets.py, set_stuff
def set_stuff(a, b):

    return set.union(a, b), set.issubset(a, b), set.issuperset(a, b)

# Lab task Number 1 of sets.py, set_intersection
def set_intersection(set1, set2):
    return set.intersection(set1, set2)

# Function to make a set from a string of tokens
def make_set(line):
    line = line.strip()
    tokens = line.split()
    return set(tokens)

def main():
    # Read in a list of strings
    lst = sys.stdin.readline().strip().split()

    # call the student's function ...
    answer = unique_list(lst)
    print(type(answer)) # should be a list
    answer.sort()
    print(answer)

if __name__ == "__main__":
    main()
