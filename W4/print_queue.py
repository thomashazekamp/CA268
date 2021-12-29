#!/usr/bin/env python3

from Queue import Queue

def print_queue(list, front, back):
    
    final_list = []
    if front < back: # if the queue hasnt circled around
        for item in list[front:back]:
            final_list.append(item)
    else:
        for item in list[front:] + list[:back]: # getting front of queue and adding the back of queue this would make the queue correct like if it was a non circular queue
            final_list.append(item)

    for i in final_list:
        print(i)

def main():
    size = int(input())
    q = Queue(size)

    command = input()
    while len(command) > 0:
        if command[0] == 'a': # add
            item = command.split()[1]
            q.enqueue(int(item))
            print(q.data, q.front, q.back)
        elif command[0] == 'r': # remove
            q.dequeue()
            print(q.data, q.front, q.back)
        else:
            print("Unknown command!")
        command = input()

    print_queue(q.data, q.front, q.back)


if __name__ == '__main__':
    main()
