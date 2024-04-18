#!/usr/bin/env python3
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0 and digits[i] + 1 >= 10:
            digits[i] = (digits[i] + 1) % 10
            i -= 1
        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        return digits

a = Solution()
result = a.plusOne([1])
print(result)