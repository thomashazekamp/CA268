#!/usr/bin/env python3


class Queue:
    def __init__(self, capacity = 4):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0

    def count(self):
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.back - self.front + len(self.data)

    def isempty(self):
        return self.front == self.back

    def enqueue(self, item):
        if self.count() < len(self.data) - 1:
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
        else:
            print("Queue Full")

    def dequeue(self):
        if self.count() > 0:
            item = self.data[self.front]
            self.front = (self.front + 1) % len(self.data)
            return item
        else:
            return None

# the following was for a queue quiz
def main():
    q = Queue()
    q.enqueue('o')
    q.enqueue('i')
    q.enqueue('e')
    x = q.dequeue()
    y = q.dequeue()
    z = q.dequeue()
    q.enqueue(y)
    q.enqueue(z)
    x = q.dequeue()
    str = ''
    while not q.is_empty():
        str += q.dequeue()
    print(str, end='')

if __name__ == '__main__':
    main()
