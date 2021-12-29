#!/usr/bin/env python3

import sys

from Stack import Stack

def reverse_input(stack):

    for line in sys.stdin.readlines():
        stack.push(line.strip())
    
    while not stack.is_empty():
        print(stack.pop())

def main():

    stack = Stack()

    reverse_input(stack)

if __name__ == '__main__':
    main()
