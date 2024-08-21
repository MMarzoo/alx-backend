#!/usr/bin/python3
"""
FU Caching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Caching class
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.lfu_freq = {}
        self.lru_arr = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.lfu_freq[key] += 1
            self.lru_arr.remove(key)
            self.lru_arr.append(key)

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.lfu_freq.values())
                min_keys = [
                    k for k, freq in self.lfu_freq.items() if freq == min_freq
                    ]

                if len(min_keys) > 1:
                    for k in self.lru_arr:
                        if k in min_keys:
                            lru_key = k
                            break

                else:
                    lru_key = min_keys[0]

                self.cache_data.pop(lru_key)
                self.lfu_freq.pop(lru_key)
                self.lru_arr.remove(lru_key)
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.lfu_freq[key] = 1
            self.lru_arr.append(key)

    def get(self, key):
        """
        Get item from cache
        """
        if key is None or key not in self.cache_data.keys():
            return None

        self.lfu_freq[key] += 1
        self.lru_arr.remove(key)
        self.lru_arr.append(key)

        return self.cache_data[key]
