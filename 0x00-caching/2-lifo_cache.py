#!/usr/bin/python3
"""
LIFO Caching
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from Basecaching and is a caching system
    """
    def __init__(self):
        """
        calling parent init
        """
        super().__init__()

    def put(self, key, item):
        """
        modifying cache data
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())
                    lenlast = len(keydel) - 1
                    del self.cache_data[keydel[lenlast]]
                    print("DISCARD: {}".format(keydel[lenlast]))
            else:
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        modifys cache data
        """
        valuecache = self.cache_data.get(key)
        return valuecache
