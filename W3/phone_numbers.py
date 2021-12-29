#!/usr/bin/env python3

import sys

def main():
    
    dict = {}

    print("Enter a name and number, or a name and ? to query (!! to exit)")
    
    while True:
        line = input()

        if line == '!!':
            print("Bye")
            break
        else:
            line = line.split()

            if line[1] != '?':
                dict[line[0]] = line[1]

            elif line[0] in dict.keys():
                print(f'{line[0]} has number {dict[line[0]]}')
                
            else:
                print(f'Sorry, there is no {line[0]}')
    

if __name__ == '__main__':
    main()
