#!/usr/bin/python3
"""
LRU Caching
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    defines LRU algo to use cache
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.leastrecent = []

    def put(self, key, item):
        """
        modify cache data
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = self.leastrecent
                    lendel = len(keydel) - 1
                    del self.cache_data[keydel[lendel]]
                    print("DISCARD: {}".format(self.leastrecent.pop()))
            else:
                del self.cache_data[key]
            if key in self.leastrecent:
                self.leastrecent.remove(key)
                self.leastrecent.insert(0, key)
            else:
                self.leastrecent.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        """
        modify cache data
        """
        valuecache = self.cache_data.get(key)
        if valuecache:
            self.leastrecent.remove(key)
            self.leastrecent.insert(0, key)
        return valuecache
