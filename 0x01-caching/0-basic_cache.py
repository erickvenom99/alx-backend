#!/usr/bin/python3
""" BaseCaching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching.
    A caching system with put and get methods
    """

    def put(self, key, item):
        """Assign key and item to the self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the item in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
