#!/usr/bin/python3
"""
Module for validUTF
"""

from typing import List


def is_continuation_byte(byte):
    """checks continuation byte"""
    return (byte >> 6) & 0b10 == 0b10


def validUtf8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid utf-8 encoding"""
    try:
        i = 0
        while i < len(data):
            if (data[i] >> 3) ^ 0b11110 == 0:
                next_n = data[(i+1):(i+4)]
                assert len(next_n) == 3 and all(is_continuation_byte(byte)
                                                for byte in next_n)
                i += 4
            elif (data[i] >> 4) ^ 0b1110 == 0:
                next_n = data[(i+1):(i+3)]
                assert len(next_n) == 2 and all(is_continuation_byte(byte)
                                                for byte in next_n)
                i += 3
            elif (data[i] >> 5) ^ 0b110 == 0:
                next_n = data[(i+1):(i+2)]
                assert len(next_n) == 1 and is_continuation_byte(next_n[0])
                i += 2
            elif (data[i] >> 7) == 0:
                i += 1
            else:
                raise ValueError("Invalid UTF-8 sequence")
    except Exception as e:
        return False
    return True
