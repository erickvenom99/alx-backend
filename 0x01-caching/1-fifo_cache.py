#!/usr/bin/python3
"""FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFOCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Add an item-value pair in self.cache_data."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = next(iter(self.cache_data))
            print(f"DISCARD: {old_key}")
            del self.cache_data[old_key]
        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is not None:
            return self.cache_data.get(key)
        return None
