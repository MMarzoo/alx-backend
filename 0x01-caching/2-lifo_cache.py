#!/usr/bin/python3
'''
LIFO Caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system '''
    def __init__(self):
        ''' Initializes the cache '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_SIZE:
            self.cache_data.popitem(last=False)
        else:
            return
        

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key
        '''
        return self.cache_data.get(key, None)
