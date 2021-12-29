#!/usr/bin/env python3

import sys

def main():
    # Opening relevant files
    with open(sys.argv[1]) as f:
        student_file = [line.rstrip() for line in f]
    with open(sys.argv[2]) as f:
        delinquent_file = [line.rstrip() for line in f]
    
    student_delinquent = []

    for student in student_file:
        if student in delinquent_file:
            student_delinquent.append(student)

    n = 1
    for i in sorted(student_delinquent):
        print(str(n) + ". " + i)
        n += 1

if __name__ == '__main__':
    main()
