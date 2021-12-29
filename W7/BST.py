#!/usr/bin/env python3

import sys
import random

#
#   Complete the recursive_count method shown below which will count all the elements in the tree
#
#   Remember what it has to do. The method needs to count the current element as well as all the
# elements of its left subtree and all the elements of its right subtree.
#
#   It can be accomplished in one return statement.
#
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
                
    ### This section is for the first task in W7 Trees labsheet

    def recursive_count(self, ptr):
        if ptr == None:  # Base Case
            return 0
        else:
            return 1 + self.recursive_count(ptr.left) + self.recursive_count(ptr.right)
                
    def count(self):
        return self.recursive_count(self.root)

    ### This section if for the second task in W7 Trees labsheet

    def count(self, low, high):
        return self.recursive_middle_count(self.root, low, high)
    
    def recursive_middle_count(self, ptr, low, high):
        if ptr is None: # Base case
            return 0
        else:
            if ptr.item >= low and ptr.item <= high:
                return 1 + self.recursive_middle_count(ptr.left, low, high) + self.recursive_middle_count(ptr.right, low, high)
            else:
                return 0 + self.recursive_middle_count(ptr.left, low, high) + self.recursive_middle_count(ptr.right, low, high)
    
    ### This section is for the third task in the W7 Trees labsheet

    def height_count(self):
        return self.recursive_height_count(self.root)

    def recursive_height_count(self, ptr):
        if ptr is None:
            return -1
        left_height = self.recursive_height_count(ptr.left)
        right_height = self.recursive_height_count(ptr.right)
        return max(left_height, right_height) + 1
    
    ### This section is for the fourth task in the W7 Trees labsheet

    def total(self):
        return self.recursive_total(self.root)

    def recursive_total(self, node):
        if node is None:
            return 0
        return node.item + self.recursive_total(node.left) + self.recursive_total(node.right)
    
    ### This section is for the fifth task in the W7 Trees labsheet

    def is_present(self, check):
        return self.recursive_is_present(self.root, check)
    
    def recursive_is_present(self, node, check):
        if node is None:
            return False
        elif check == node.item:
            return True
        else: # This recursion keeps going until the code above returns False(meaning end of tree) or True(meaning the item we are checking does exist)
            l_check = self.recursive_is_present(node.left, check)
            r_check = self.recursive_is_present(node.right, check)
            if l_check or r_check is True: # If either are True then the item does exist
                return True
            else:
                return False # This means the l_check and r_check both did not return with True
    
    ### This section is for the sixth task in the W7 Trees labsheet

    def count_leaves(self):
        return self.recursive_count_leaves(self.root)
    
    def recursive_count_leaves(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        return self.recursive_count_leaves(node.left) + self.recursive_count_leaves(node.right)
        

        

##### This main function is for the first task for the Trees labsheet W7

# def main():
#     line = sys.stdin.readline()
#     nums = line.strip().split()

#     bst = BST()
#     print(bst.count()) # This should print 0 since no numbers have been added

#     for num in nums:
#         bst.add(num)
    
#     print(bst.count()) # Printing after all numbers have been added to the binary search tree


# if __name__ == '__main__':
#     main()

##### This main func is for the second task for the Trees labsheet W7

# def main():
#     bst = BST()
    
#     for ele in [2, 7, 4, 8, 5]:
#         bst.add(ele)
    
#     print(bst.count(3, 5))

# if __name__ == '__main__':
#     main()

##### The following main function is for the third task in the Trees labsheet W7

# def main():
#     line = sys.stdin.readline()
#     nums = line.strip().split()

#     bst = BST()

#     for num in nums:
#         bst.add(num)

#     print(bst.height_count())

# if __name__ == '__main__':
#     main()

### The follwiing main function is for the fourth task in the Trees labsheet W7

# def main():
#     line = sys.stdin.readline()
#     nums = line.strip().split()

#     bst = BST()

#     for num in nums:
#         bst.add(int(num))

#     print(bst.total())

# if __name__ == '__main__':
#     main()

### The following main function is for the fifth task in the Trees labsheet W7

# def main():
#     line = sys.stdin.readline()
#     nums = line.strip().split() # test case nums = [1, 2, 3, 4, 5]

#     bst = BST()

#     for num in nums:
#         bst.add(int(num))

#     print(bst.is_present(1)) # This shold print True since 1 is is the test case

# if __name__ == '__main__':
#     main()

### The following main function is for the sixth task in the Trees labsheet W7

# def main():
#     line = sys.stdin.readline()
#     nums = line.strip().split() # test case nums = [1, 2, 3, 4, 5]

#     bst = BST()

#     for num in nums:
#         bst.add(int(num))

#     print(bst.count_leaves())

# if __name__ == '__main__':
#     main()

### This make_list function is for the seventh task in the Trees W7 Labsheet

def make_list(lst):
    if lst == []: # Base case
        return []
    
    sorted_list = sorted(lst) # Initially sorting the list

    middle_index = len(sorted_list) // 2 # Each time we check the list we want the middle value of the sorted list/sublist
    return [sorted_list[middle_index]] + make_list(sorted_list[middle_index + 1:] + make_list(sorted_list[:middle_index]))


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