#!/usr/bin/env python3
"""MRU Caching module"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """A MRUCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add key, value items to cache."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.order[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_item = list(self.order)[-1]
            print("DISCARD: {}".format(mru_item))
            del self.cache_data[mru_item]
            del self.order[mru_item]
        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
