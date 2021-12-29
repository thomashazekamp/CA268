#!/usr/bin/env python3

import sys
import random

class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree
     """
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for x in lst:
                self.add(x)

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): return self.r_height(self.root)

# Start of main function
# def main():
#     # Read each test case
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]

#     tree = BST(nums)

#     if tree.height() > 2:
#          print("error ... your tree is too tall")
#     else:
#          print(tree.is_avl())

# if __name__ == "__main__":
#     main()

### This make_list function is for the seventh task in the Trees W7 Labsheet

def make_list(lst):
    if lst == []: # Base case
        return []
    
    sorted_list = sorted(lst) # Initially sorting the list

    middle_index = len(sorted_list) // 2 # Each time we check the list we want the middle value of the sorted list/sublist
    return [sorted_list[middle_index]] + make_list(sorted_list[:middle_index]) + make_list(sorted_list[middle_index + 1:])


##### The following main function is for the seventh task in the Trees labsheet W7

def main():
    random.seed(0)
    
    for length in [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 50, 100]:
        # Make a random lst
        lst = random.sample(range(length), length)

        # Use the students function to arramge the list
        new_list = make_list(lst) # get the student's lst

        # Make sure they have the same elements
        if sorted(lst) != sorted(new_list):
            print("You have somehow changed the elements of the list. You are only supposed to change the order.")
        else:
            # Create a BST
            tree = BST()
            # and add in the elements from the list
            for element in new_list:
                tree.add(element)
            # Show the lst
            print(lst)
            # And some data ... the height, the count and whether or not balanced.
            print(tree.max_height(), tree.count(), tree.is_balanced())

if __name__ == "__main__":
    main()