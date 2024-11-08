#!/usr/bin/env python3

"""
A simple Pagination module
"""

import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start and end
    index that correspond to the range of index in
    a pagination parameter.
    Args:
        - page (int): The page number (1-indexed)
        - page_size (int): The size of each page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """
        Get a page from the dataset.
        Args:
            - page (int): The page number (1-indexed)
            - page_size (int): The size of each page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        total_size = len(data)
        if start_index >= total_size:
            return []

        return data[start_index:end_index]
