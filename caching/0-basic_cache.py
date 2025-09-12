#!/usr/bin/env python3
"""
Basic Cache Module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system with no limit.
    Uses the inherited dictionary cache_data for storage.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Return None if key is None or
        the key doesn't exist in cache_data.
        """
        return self.cache_data.get(key, None)