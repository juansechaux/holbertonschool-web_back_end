#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that
multiplies a float by multiplier
"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''make_multiplier function that takes a float
    multiplier as argument and returns a function that
    multiplies a float by multiplier'''
    def multiplier_function(x: float) -> float:
        '''Function that takes a float and multiplies
        by multiplier'''
        return x * multiplier

    return multiplier_function
