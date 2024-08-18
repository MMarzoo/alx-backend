#!/usr/bin/env python3
'''
Implementation of (get_page) function to paginate a database.
'''

import csv
from math import ceil
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple of size two containing a start index and an end index'''
    return ((page-1) * page_size, page_size * page)


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
        ''' get_page retrieves a specified page of the list '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]
        dataset = self.dataset()
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' get_hyper retrieves a specified page of the list '''
        page_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page != 1 else None,
            "total_pages": total_pages
        }
