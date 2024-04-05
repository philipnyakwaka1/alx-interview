#!/usr/bin/python3
from typing import List
"""
[1] 
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
"""
#Loop n times
#base cases defined i.e when n = 1 or n = 2

def find_pascal(n):
    my_list = [[1], [1, 1]]
    for i in range(2, n):
        row = []
        for j in range(len(my_list[i - 1]) - 1):
            num = my_list[i - 1][j] + my_list[i - 1][j + 1]
            row.append(num)
        row.append(1)
        row.insert(0, 1)
        my_list.append(row)
    return [[1]] if n == 1 else [] if n <= 0 else my_list
l = find_pascal(5)
for _ in l:
    print(_)

