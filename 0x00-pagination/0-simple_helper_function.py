#!/usr/bin/env python3

"""
Module is a function named index_range that takes two integer
argument and return a tuple of size two containing a start and
end index correspondoing to range of indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
