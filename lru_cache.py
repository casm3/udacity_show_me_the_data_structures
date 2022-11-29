import unittest
from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def __len__(self):
        return len(self.cache)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        return self.cache[key] if self.cache.get(key) else -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        self.cache[key] = value
        self.cache.move_to_end(key)
        if self.capacity < len(self.cache):
            self.cache.popitem(last=False)


class TestLRUCache(unittest.TestCase):
    def setUp(self) -> None:
        self.cache = LRU_Cache(3)
        self.cache.set(1, 1)
        self.cache.set(2, 2)
        self.cache.set(3, 3)

    def test_constructor(self):
        assert self.cache.capacity == 3

    def test_set(self):
        assert len(self.cache) == 3
        self.cache.set(4, 4)
        assert len(self.cache) == 3

    def test_get(self):
        # removes oldest element
        self.cache.set(4, 4)
        assert self.cache.get(1) == -1
        assert self.cache.get(4) == 4

    def test_set_none(self):
        self.cache.set(4, None)
        assert self.cache.get(4) == -1

    def test_set_bigger_values(self):
        self.cache.set(10000, 10000)
        assert self.cache.get(10000) == 10000


if __name__ == "__main__":
    unittest.main()
