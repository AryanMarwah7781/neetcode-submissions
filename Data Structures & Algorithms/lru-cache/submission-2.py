class cacheNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # head is least recent, tail is most recent
        self.head = cacheNode(0,0)
        self.tail = cacheNode(0,0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    # remove from the list
    def remove(self, node):
        # node is always a middle node
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    # insert at the tail -- most recent
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # remove from list
            self.remove(self.cache[key])
            # update the order by adding at the tail -- MRU
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1
        
    def put(self, key: int, value: int) -> None:
        # remove node if it already exists
        # will add the new node
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = cacheNode(key, value)
        self.insert(self.cache[key])

        # now check if the length is exceeded
        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the hashmap
            lru = self.head.nxt
            self.remove(lru)
            del self.cache[lru.key]
        