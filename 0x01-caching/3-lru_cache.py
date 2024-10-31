#!/usr/bin/env python3
"""LRU Caching module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """A LRUCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add an item-value pair in self.cache_data."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.order[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_item = next(iter(self.order))
            print("DISCARD: {}".format(least_item))
            del self.cache_data[least_item]
            del self.order[least_item]
        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
