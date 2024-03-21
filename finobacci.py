#!/usr/bin/env python3
from typing import List
def finobacci(n: int) -> List[int]:
    if n > 0:
        my_list = [0, 1]
        for i in range(2, n):
            my_list.append(my_list[i - 1] + my_list[i - 2])
    return my_list[:n]
print(finobacci(5))