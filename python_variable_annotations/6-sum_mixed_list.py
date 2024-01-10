#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a
list input_list of floats as argument and returns
their sum as a float
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    '''concat function that takes imput_list of floats and return
    a sum of all floats'''
    result: float = 0
    for value in mxd_lst:
        result += value
    return result
