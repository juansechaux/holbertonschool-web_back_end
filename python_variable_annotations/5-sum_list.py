#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a
list input_list of floats as argument and returns
their sum as a float
"""


def sum_list(imput_list: list[float]) -> float:
    '''concat function that takes imput_list of floats and return
    a sum of all floats'''
    result: float = 0
    for value in imput_list:
        result += value
    return result
