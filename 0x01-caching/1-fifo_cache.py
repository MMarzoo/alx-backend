#!/usr/bin/python3
'''
FIFO caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    '''
    class FIFOCache that inherits from BaseCaching and is a caching system
    '''

    def __init__(self):
        ''' INit '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.cache_data.popitem(False)
            print(f"DISCARD: {first_key[0]}")

    def get(self, key):
        ''' return the value in self.cache_data linked to key '''
        return self.cache_data.get(key, None)
