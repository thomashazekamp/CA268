#!/usr/bin/env python3

def make_map():

  import sys
  whatever = sys.stdin.readlines()
  grades = {}
  for line in whatever:
    line = line.rstrip().split()
    if line == []:
      pass
    else:
      grades[line[0]] = line[1]
    
  return grades
