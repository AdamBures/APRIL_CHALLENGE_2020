from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict
            
        self.cache[key] = value
