
from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

        
    def push(self, item):
        self.ll.add(item)
        
    def pop(self):
        return self.ll.remove()
        
    def is_empty(self):
        return self.ll.is_empty()

def main():
    stack = LinkedStack()
    
    tests = []
    
    tests.append(stack.is_empty())  # check the stack is empty first.
    tests.append(stack.pop() == None)
    
    val = 9
    stack.push(val)
    tests.append(not stack.is_empty())
    tests.append(stack.pop() == val)

    vowels = "aeiou"
    for c in vowels:
        stack.push(c)

    contents = ""
    while not stack.is_empty():
        contents += stack.pop()
        
    tests.append(vowels == contents[::-1])
    
    if all(tests):
        print("OK")
    else:
        print("Failed tests: ", end = "")
        for i in range(len(tests)):
            if not tests[i]:
                print(i, end = " " )
        print()

if __name__ == '__main__':
    main()
