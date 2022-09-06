#!/usr/bin/env python3
"""
Basic Dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:
      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello
      >>> print(my_cache.get("A"))
      Hello
    """
    def put(self, key, item):
        """
        key of dictionary is the value of the key
        """
        if key or item is not None:
            self.cache_data[key] = item
    def get(self, key):
        """
        gets key and returns value of said key
        """
        valuecache = self.cache_data.get(key)
        return valuecache
