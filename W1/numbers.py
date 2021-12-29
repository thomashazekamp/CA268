#!/usr/bin/env python3

import sys

list = [3, 4, 5]
sum = 8

def sum_to_k(nums_list, num_sum):
    #nums_list = set(" ".join(nums_list))
    
    for i in range(len(nums_list)):
        for j in range(i + 1, len(nums_list)):
            if nums_list[i] + nums_list[j] == num_sum:
                print(nums_list[i], nums_list[j])
sum_to_k(list, sum)