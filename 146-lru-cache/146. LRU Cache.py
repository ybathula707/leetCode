class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        #orderedDictionaries already store items in order
        #no need to declare LL since this ds handles ordering + lookups
        
    # if in cache -> return and move to end. Else ret -1
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key] # returns node val @ key 
        
    # if in cache -> move to end & update put val. Pop last item if full
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)