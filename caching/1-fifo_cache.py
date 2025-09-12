#!/usr/bin/env python3
"""
FIFO Cache Module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system where the first item added
    is the first one to be discarded
    once the cache reaches its limit.
    """

    def __init__(self):
        """
        Initialize the cache system and keep track
        of the order of items.
        """
        super().__init__()
        self.order = []  # To maintain the order of the cache items

    def put(self, key, item):
        """
        Add an item in the cache using FIFO policy.
        If key or item is None, do nothing.
        If cache exceeds MAX_ITEMS,
        discard the first item added and print the key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in_key = self.order.pop(0)
            del self.cache_data[first_in_key]
            print(f"DISCARD: {first_in_key}")

    def get(self, key):
        """
        Get an item by key.
        Return None if the key is None or doesn't exist.
        """
        return self.cache_data.get(key, None)
    