#!/usr/bin/env python3

import sys

# Stack class

class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]

# Start of program task

def check_brackets(line):
    stack = Stack()

    brackets = {'(' : ')', '[' : ']', '{' : '}'}

    for i in line:
        if i == '(' or i == '[' or i == '{':
            stack.push(i) # adding each opening bracket to the stack
        elif i == ')' or i == ']' or i == '}':
            if stack: # if the stack is not empty continue with the following
                if stack.is_empty() is True: # check that the stack is not already empty eg [')'] this would automatically give a mismatch/error
                    return False
                else:
                    top = stack.pop()
                    if brackets[top] != i: # if the item on top of stack does not match to the same dict item (its opposite bracket) then its a mismatch
                        return False
            else:
                return False
    return stack.is_empty()



def main():
    line = sys.stdin.readline()

    result = check_brackets(line)

    if result is True:
        print(f'check_brackets({line}) is true')
    else:
        print(f'check_brackets({line}) is false')
    

if __name__ == '__main__':
    main()
