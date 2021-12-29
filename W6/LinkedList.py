#!/usr/bin/env python3

# This program is for Week 6 lab tasks using recursion
import sys

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
    
    # count and recursive count is for the first task
    def count(self):
        return self.recursive_count(self.head) # Calling the recursive function, this only happends once
    
    def recursive_count(self, node):
        if node is None:
            return 0
        return self.recursive_count(node.next) + 1

    # In the testing on poodle this function is called count_even()
    def even_count(self): # even_count and recursive_even_count is for the second task for the recursive lab
        return self.recursive_even_count(self.head)

    def recursive_even_count(self, node):
        if node is None:
            return 0
        if (int(node.item) % 2 == 0):
            return self.recursive_even_count(node.next) + 1
        else:
            return self.recursive_even_count(node.next)
        
    def is_present(self, item):
        return self.is_present_recursive(self.head, item)
    
    def is_present_recursive(self, node, item):
        if node is None:
            return False
        elif node.item == item:
            return True
        else:
            return self.is_present_recursive(node.next, item)
    
    def largest(self):
        largest = self.head.item
        return self.largest_recursive(self.head, largest)
    
    def largest_recursive(self, node, largest):
        if node is None:
            return largest
        else:
            if node.item > largest:
                largest = node.item
            return self.largest_recursive(node.next, largest)
    
    def duplicates(self):
        return self.duplicates_recursive(self.head)
    
    def duplicates_recursive(self, node):
        if node is None:
            return False
        else:
            if node.next is not None:
                if node.item == node.next.item:
                    return True
        return self.duplicates_recursive(node.next)


### This main function is for the first lab task of Week 6 - A recursive count

# def main():
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
    
#     ll = LinkedList()
#     # call the students function
#     print(ll.count())   # Empty list, count should return 0
    
#     for item in items:
#         ll.add(item)
    
#     # call the students function
#     print(ll.count())
    
#     # check that the first item removed from the list is the same as the last one added
#     same = ll.remove() == items.pop()
    
#     # call the students function again ... should be one shorter.
#     print(ll.count())
    
#     while not ll.is_empty() and len(items) > 0:
#         same = same and ll.remove() == items.pop()
        
#     if not same or not ll.is_empty() or len(items) != 0:
#         print("the list has been modified!")
    

# if __name__ == "__main__":
#     main()

### This main is used for the second lab task of the recursion lab sheet

# def main():
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]
    
#     ll = LinkedList()
    
#     for num in nums:
#         ll.add(num)
    
#     print(ll.even_count()) # in the testing this is count_even

# if __name__ == "__main__":
#     main()

### This main function is used for the third lab task of the recursion lab sheet

# def main():
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
    
#     ll = LinkedList()
#     problem = False
#     if ll.is_present(items[0]) and items[0]:
#         print("An empty list should not match anything")
#         problem = True
    
#     else:
#         for item in items:
#             if ll.is_present(item) and item:
#                 print(item + " detected before being added.")
#                 problem = True
#             ll.add(item)
            
#         # Now every item in the items should be in the list.
#         for item in items:
#             if not ll.is_present(item): # item should not be contained
#                 print(item + " not found in list.")
#                 problem = True

#     if not problem:
#         # check that the list still contains all the items
#         while not ll.is_empty() and len(items) > 0:
#             if ll.remove() != items.pop():
#                 print("List has been modified")
#                 problem = True
#                 break
        
#         if not problem:
#             if (not ll.is_empty()) or len(items) != 0:
#                 print("the list size is wrong")
#                 problem = True
                
#     if problem:
#         print("More work nned!")
#     else:
#         print("all ok!")

# if __name__ == "__main__":
#     main()

### The following main function is for the fourth task of the recursion week

# def main():
#     # Create a list for the tests
#     tests = []
    
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items] # Create an array of nums from the strings
    
#     ll = LinkedList()

#     # Add each number to the list
#     for num in nums:
#         ll.add(num)
    
#     # call the students function
#     tests.append(ll.largest() == max(nums)) # First test ... compare students function to max
    
#     # Keep reducing the list, comparing the largest of the reduced list to the remiaining numbers.
#     count = 1
#     while count == len(nums):
#         ll.remove() # Remove one element from the list
#         # Compare the largest of this list with the remaining numbers
#         tests.append(ll.largest() == max(nums[count:]))
#         count += 1
        
#     if all(tests):
#         print("All tests passed!")
#     else:
#         for i in range(len(tests)):
#             if not tests[i]:
#                 print("test " + str(i) + " failed.")

# if __name__ == "__main__":
#     main()

### The following main function is for the fifth task of the recursion lab sheet

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    bool = str(ll.duplicates())[0]
    print(bool, end="")  # Only print the first letter of the result (F for false, T for true)
    for item in items:
        ll.add(item)
        bool = str(ll.duplicates())[0] # Only print the first letter of the result
        print(bool, end="")
        
    print()

if __name__ == "__main__":
    main()