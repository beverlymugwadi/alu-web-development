#!/usr/bin/env python3
"""
LRU Cache Module
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system where the
    least recently used item is discarded
    when the cache exceeds the limit.
    """

    def __init__(self):
        """
        Initialize the cache system and track the order of usage.
        """
        super().__init__()
        self.usage_order = []  # To track the usage order of the cache items

    def put(self, key, item):
        """
        Add an item to the cache using the LRU policy.
        If key or item is None, do nothing.
        If the cache exceeds MAX_ITEMS, discard
        the least recently used item.
        """
        if key is None or item is None:
            return

        # If key already exists, remove it to update its usage order
        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        # Check if the cache exceeds the limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Get an item by key.
        Return None if the key is None or doesn't exist in cache_data.
        If the key is found, update its usage order.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order by moving accessed key to the end
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data.get(key)
    