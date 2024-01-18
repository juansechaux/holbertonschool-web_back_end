#!/usr/bin/env python3
'''
function named index_range that takes two integer arguments page and page_size
'''
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Retrieve a specific page of data from a CSV file.
        '''
        assert type(page) is int and type(page_size) is int, "Must be int"
        assert page > 0 and page_size > 0, "The page and page_size must be > 0"
        list_of_data = []
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            indexes = index_range(page, page_size)
            for num, line in enumerate(reader):
                if num in range(indexes[0], indexes[1]):
                    list_of_data.append(line)
        return list_of_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''method that takes the same arguments (and defaults)as get_page
        and returns a dictionary containing the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        '''
        dict_of_data = {}
        indexes = index_range(page, page_size)
        dict_of_data["page_size"] = indexes[1] - indexes[0]
        dict_of_data["page"] = indexes[0] + 1
        dict_of_data["data"] = self.get_page(page, page_size)
        total_pages = len(self.dataset())
        if total_pages <= (indexes[0] + 2):
            dict_of_data["next_page"] = None
        elif total_pages != (indexes[0] + 2):
            dict_of_data["next_page"] = dict_of_data["page"] + 1
        if indexes[0] == 0:
            dict_of_data["prev_page"] = None
        elif indexes[0] != 0:
            dict_of_data["prev_page"] = dict_of_data["page"] - 1
        dict_of_data["total_pages"] = total_pages
        return dict_of_data


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return tuple([start_index, end_index])
