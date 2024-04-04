#!/usr/bin/python3
"""
Module for validUTF
"""

from typing import List


def validUtf8(data: List[int]) -> bool:
        """checks if data set is a valid utf-8 encoding"""
        count = 0
        for byte in data:                          
            byte|= 256 

            if (byte >> 3 == 0b1_11111 or 
                (byte >> 6 == 0b1_10)^(count>0)):
                return False
            if byte >> 6 == 0b1_10:
                count = count - 1
            elif byte >> 4 == 0b1_1111:
                count = 3
            elif byte >> 4 == 0b1_1110:
                count = 2
            if   byte >> 5 == 0b1_110 :
                count = 1

        return not count
