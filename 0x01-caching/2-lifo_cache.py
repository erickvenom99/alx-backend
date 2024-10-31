#!/usr/bin/python3
"""LIFOCache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFOCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Add an item-value pair in self.cache_data."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_item}")
            del self.cache_data[last_item]
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None:
            return None
        return self.cache_data.get(key)
