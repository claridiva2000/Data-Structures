from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit =limit
        self.dl_list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        for k in self.storage:
            if k == key:
                # get value
                value = self.storage[k]
                # remove key value
                self.storage.pop(k)
                # set key & value as most recently used
                self.set(k, value)
                # return value
                return self.storage[k]

        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        pop_lru = None
        # if key already exists, replace it with the current value
        if self.storage.get(key):
            self.storage[key] = value

        # if the dict is already at the limit, iterate through the keys
        elif self.limit == len(self.storage):
            for i, k in enumerate(self.storage):
                # the least recently used key will be at index 0
                if i == 0:
                    pop_lru = k
                    # remove lru
                    self.storage.pop(pop_lru)
                    # replace with the new value
                    self.storage[key] = value
                    break
        # if not at the limit, just add it to the dict
        else:
            self.storage[key] = value
