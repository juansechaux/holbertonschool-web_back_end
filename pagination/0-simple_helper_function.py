#!/usr/bin/env python3
'''
function named index_range that takes two integer arguments page and page_size
'''


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return tuple([start_index, end_index])
