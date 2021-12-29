### Answer to first task of Radix sort (first iteration of sorting algo)
# def sol():
#     return ['0010', '0000', '1110', '1011', '1001', '0111']

### Answer to second task of Radix sort (Third iteration of sorting algo)
# def sol():
#     return ['0000', '1001', '0010', '1011', '1110', '0111']

### Answer to third task of Radix sort

# The initial list is [262, 37, 111, 105, 103, 189, 239, 270, 38, 43, 246]

# def sol():
#     return [[270], [111], [262], [103, 43], [], [105], [246], [37], [38], [189], [239]]

### For the fourth task its using same list as above (returning list of 10 buckets in a list), this is the second pass of the above list

def sol():
    return [[103, 105], [111], [], [37, 38, 239], [43, 246], [], [262], [270], [189], []]


##### This is the last task creating the sorting algo

#!/usr/bin/env python3

def radixsort(lst, num):
   # for each power of two (starting at lowest) sort based on that power
   for p in range(num):  # Assume 6 bits
      # Split list in two
      lo = [x for x in lst if x & (1 << p) == 0] # lo where the bit is zero
      hi = [x for x in lst if x & (1 << p) != 0] # hi where the bit is one
      lst = lo + hi # combine the two into one list.

   return lst
