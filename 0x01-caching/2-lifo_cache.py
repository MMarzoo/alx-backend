#!/usr/bin/python3
'''
LIFO Caching
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        ''' Initializes the cache. '''
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                self.cache_data.pop(self.last_key)
                print(f'DISCARD: {self.last_key}')

        self.last_key = key

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        '''
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
