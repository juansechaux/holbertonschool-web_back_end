#!/usr/bin/env python3
"""
functions parameters and return values with the appropriate types
"""
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input iterable.

    Parameters:
    - lst (Iterable[Sequence]): An iterable containing elements of type Sequence.

    Returns:
    - List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element from the input iterable
      and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
