#!/usr/bin/python3
'''
LRU Caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    LRU Caching class
    '''
    def __init__(self):
        '''
        inInitializes the cache
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key
        '''
        if key is None and key not in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
