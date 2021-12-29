#!/usr/bin/env python3

import sys

#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item): # Method to add an item to the linked list
        self.head = Node(item, self.head)

    def remove(self): # Method to remove an item from the linked list
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self): # Method to check if the linked list is empty
        return self.head == None
    
    def count(self): # Method to get the total number of items(nodes) in the linked list
        if self.is_empty() is True:
            return 0
        else:
            check = self.head
            count = 0
            while check is not None:
                count = count + 1
                check = check.next
            return count
    
    def contains(self, item): # Method to check if the item given is contained in the linked list
        check = self.head
        while check is not None:
            if check.item == item:
                return True
            check = check.next
        return False
    
    def after(self, item): # Method to get the item after the given one
        check = self.head
        while check is not None:
            if check.item == item:
                check = check.next
                return check.item
            check = check.next
        return None
    
    def before(self, item): # Method to get the item before a given one
        check = self.head
        c_copy = self.head
        i = 0
        while check is not None:
            if item == check.item:
                check = check.next
                return c_copy.item
            check = check.next
            if i == 1:
                c_copy = c_copy.next
            i = 1
        return None
    
    def __str__(self): # Method to print the linked list when str() function is called upon it
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next
        
        return tmp_str
    
    def rotate(self):
        current = self.head
        if current is None:
            return
        tmp = current
        while current.next is not None:
            current = current.next
        current.next = self.head
        self.head = tmp.next
        tmp.next = None


########
# main function for Linked lists task number 1
########

# def main():
#         # Read each set
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
#         print("the list has been modified!");


# if __name__ == '__main__':
#     main()

########
# Main function for task number 2 in linked list tasks
########

# def main():
#     # Read each line
#     line = sys.stdin.readline()
#     items = line.strip().split()
    
#     ll = LinkedList()
#     problem = False
#     if ll.contains(items[0]):
#         print("An empty list should not match anything")
#         problem = True
    
#     else:
#         for item in items:
#             if ll.contains(item):
#                 print(item + " detected before being added.")
#                 problem = True
#             ll.add(item)
            
#         # Now every item in the items should be in the list.
#         for item in items:
#             if not ll.contains(item): # item should not be contained
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
#         print("More work needed!")
#     else:
#         print("all ok!")

# if __name__ == "__main__":
#     main()

########
# Main function for task 3 in linked lists week
########

# def main():
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
    
#     tests = [] # list of the results of the tests
    
#     ll = LinkedList()

#     # Check that it works for an empty list    
#     tests.append(ll.after("") == None)  # Each test should be True

#     # Check that the item doesn't exist before it is added    
#     for item in items:
#         tests.append(ll.after(item) == None)
#         ll.add(item)
    
#     items.reverse()
#     for i in range(len(items) - 1):
#         print(ll.after(items[i]), items[i+1])
#         tests.append(ll.after(items[i]) == items[i+1])
        
#     print("All Good" if all(tests) else str(tests))

# if __name__ == "__main__":
#     main()

########
# Main function for task 4 in linked list tasks
########

# def main():
#     # Read each set
#     line = sys.stdin.readline()
#     items = line.strip().split()
    
#     # A list to store the results of the tests
#     tests = []
    
#     ll = LinkedList()

#     # Check that it works for an empty list    
#     tests.append(ll.before("") == None)  # Each test should be True

#     # Check that the item doesn't exist before it is added    
#     for item in items:
#         tests.append(ll.before(item) == None)
#         ll.add(item)
    
#     items.reverse()
#     for i in range(len(items) - 1):
#         # print(ll.before(items[i + 1]), items[i])
#         tests.append(ll.before(items[i + 1]) == items[i])
        
#     print("All Good" if all(tests) else str(tests))

# if __name__ == "__main__":
#     main()

########
# Main function for task 7 in linked list tasks
########

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()

    # Create the linked list
    ll = LinkedList()

    # add the items to the linked list
    for item in items:
        ll.add(item)

    # print the linked list
    print(str(ll))
    ll.rotate() # rotate it
    print(str(ll)) # print it again

    # create the list using append 
    for i in range(len(items)-1):
        ll.rotate() # Rotate enough times should get back to the original
    print(str(ll))

if __name__ == "__main__":
    main()