#!/usr/bin/env python3

l = [4, 4, 2, 10]

def calc_average(list):
    sum_num = sum(list) // len(list)
    return sum_num

# print(calc_average(l))

def above_average(list):
    sum_num = sum(list) // len(list)
    new_list = []
    for i in list:
        if i > sum_num:
            new_list.append(i)
    return new_list

# print(above_average(l))