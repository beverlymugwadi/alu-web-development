#!/usr/bin/python3
""" LFU Caching Module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.freq = {}       # Track frequency of use
        self.order = {}      # Track order for LRU tie-breaking
        self.counter = 0     # Global counter for order

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        # Insert or update item
        self.cache_data[key] = item
        # Update frequency
        self.freq[key] = self.freq.get(key, 0) + 1
        # Update order (for LRU in case of tie)
        self.counter += 1
        self.order[key] = self.counter

        # If cache exceeds max size -> remove LFU (or LRU of LFU)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the minimum frequency
            min_freq = min(self.freq.values())
            # Candidates = all keys with min frequency
            candidates = [
                k for k, v in self.freq.items() if v == min_freq
            ]
            if len(candidates) == 1:
                discard_key = candidates[0]
            else:
                # Apply LRU among candidates
                discard_key = min(candidates, key=lambda k: self.order[k])

            # Remove from all tracking dicts
            del self.cache_data[discard_key]
            del self.freq[discard_key]
            del self.order[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Increase frequency and update order
        self.freq[key] += 1
        self.counter += 1
        self.order[key] = self.counter

        return self.cache_data[key]
