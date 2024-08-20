#!/usr/bin/python3
'''
Basic dictionary
'''


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache class. Inherits from BaseCaching '''

    def put(self, key, item):
        ''' assign to the dictionary self.cache_data the
        item value for the key key
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' return the value in self.cache_data linked to key '''
        if key in self.cache_data:
            return self.cache_data[key]
