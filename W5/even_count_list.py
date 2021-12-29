#!/usr/bin/env python3

import sys
from LinkedList import LinkedList

def even_count(lst):
    check = lst.head
    count = 0
    while check is not None:
        if check.item % 2 == 0:
            count = count + 1
        check = check.next
    return count


def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))

if __name__ == "__main__":
    main()