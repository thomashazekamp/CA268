#!/usr/bin/env python3

import sys

#
#  This linked list use built-ins: str(), iter(), len(), in()
#
#   These functions are implemented using recursion (except iter)
#
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

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)

    def recursive_contains(self, ptr, item):
        if ptr == None:
            return False
        else:
            return item == ptr.item or self.recursive_contains(ptr.next)

    def __in__(self, item):
        return self.recursive_contains(self.head, item)

    def recursive_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.item) + "->" + self.recursive_str(ptr.next)

    def __str__(self):
        return self.recursive_str(self.head)

### This is the HashSet class

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)
        check = 0

        if self.table[index] != None: # The check changes if there is a collision
            check = 1

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
        
        if check == 1: # This returns the index of the collision and the item
            return (index, item)
        return None
    
    # Function for getting the average size of each index and its linked list
    def average_bucket_length(self):
        total = 0
        total_count = 0
        index = 0

        while index != len(self.table):
            if self.table[index] != None:
                total = total + len(self.table[index])
                total_count += 1 # Counting the total number of linked lists
            index += 1
        return total / total_count
    
    # Function for getting the min and max of legths of the linked lists
    def min_max_bucket_length(self):
        min = 0
        max = 0

        for index_value in self.table:
            if index_value != None:
                if len(index_value) > max:
                    max = len(index_value)
                if min == 0 or len(index_value) < min:
                    min = len(index_value)
        return (min, max)

    # This function can iterate through the hash set and linked list
    def __iter__(self):
        for index_value in self.table: # Iterating through the table
            if index_value != None: # If the index is not empty
                for item in index_value: # Iterating through the linked list
                    yield item

### This is the main function for the first task in the Hash lab sheet

# def main():
#     # Read each test case
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]
    
#     # First number is the capacity
#     numset = HashSet(nums[0])

#     for x in nums[1:]:
#         print(str(numset.add(x)) + " ", end="")

#     print()

# if __name__ == "__main__":
#     main()

###### The following main function is for the second Hashing lab task

# def main():
#     # Read each test case
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]
    
#     # First number is the capacity
#     numset = HashSet(nums[0])

#     for x in nums[1:]:
#         numset.add(x)

#     print(numset.average_bucket_length())

# if __name__ == "__main__":
#     main()

###### The following main function is for the third lab task (Hashing)

# def main():
#     # Read each test case
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]
    
#     # First number is the capacity
#     numset = HashSet(nums[0])

#     for x in nums[1:]:
#         numset.add(x)

#     print(numset.min_max_bucket_length())

# if __name__ == "__main__":
#     main()

###### The following main function is for the fourth lab task (Hashing)

# def main():
#     # Read each test case
#     line = sys.stdin.readline()
#     items = line.strip().split()
#     nums = [int(item) for item in items]
    
#     # First number is the capacity
#     numset = HashSet(nums[0])

#     for x in nums[1:]:
#         numset.add(x)
        
#     numset_items = []
#     for x in numset:
#         numset_items.append(x)

#     print(sorted(numset_items))

# if __name__ == "__main__":
#     main()
### Test to see how yield works for the above main function & task
# list = [1, 2, 3, 4, 5]
# def test(list):
#     for num in list:
#         yield num

# print(sorted(test(list), reverse=True))

###### The  fifth lab task (Hashing) is in the python file HashSet2.py

###### The sixth lab task (Hashing) is in the python file HashSet3.py

