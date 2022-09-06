#!/usr/bin/python3
"""
FIFO Cache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First in first out algorithm
    """
    def __init__(self):
        """
        initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        modifys the cache data
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[0]
                    del self.cache_data[keydel]
                    print("DISCARD: {}".format(keydel))
            self.cache_data[key] = item

    def get(self, key):
        """
        key for dicitonary
        returns value of key
        """
        valuecache = self.cache_data.get(key)
        return valuecache
