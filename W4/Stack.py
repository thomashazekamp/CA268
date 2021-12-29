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

# the following was for the stack quiz

def main():
   s = Stack()
   s.push('o')
   s.push('i')
   s.push('e')
   x = s.pop()
   y = s.pop()
   z = s.pop()
   s.push(y)
   s.push(z)
   x = s.pop()
   str = ''
   while not s.is_empty():
      str += s.pop()
   print(str, end='')

if __name__ == '__main__':
    main()
