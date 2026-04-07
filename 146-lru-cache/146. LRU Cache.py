#Creating the Node Class

class ListNode:
    def __init__(self, key, value):
        self.key = key
        # key is the access order of this cache items (index in the LL)

        self.val = value
        # value of the node

        self.next = None
        self.previous = None


class LRUCache:
    # doubly linked list w/ hash map for O(1) lookups
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        # new list head points to tail
        self.tail.previous = self.head
        # new list tail prev ref to head

        self.cache_keys = {} 
        # will contain key:node mapping of nodes in Cache LL to give O(1) lookups

    def get(self, key: int) -> int:
        '''
            Return node if hashmap contains it, move node to end.
            Return -1 otherwise

        '''
        if key not in self.cache_keys:
            return -1

        node = self.cache_keys[key]
        self.delete(node)
        self.add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        '''
            If node already exists, remove node and add to end.
            If at capacity, remove node at head before adding to end
        '''
        if key in self.cache_keys:
            old_node = self.cache_keys[key]
            self.delete(old_node)

        node = ListNode(key, value)
        self.cache_keys[key] = node
        self.add_to_end(node)

        # check capacity and evict head (oldest) if reached
        # evict --> 1) delete node from LL 2)delete key from cache key hash
        if len(self.cache_keys) > self.capacity:
            node_delete = self.head.next
            self.delete(node_delete)
            del self.cache_keys[node_delete.key]



    # Insert node to end of the list (inserting at end give us O(1) time complexity)
    def add_to_end(self, node: ListNode):
        ''' 
            1. track the end of LL (tail.previous)
            2. set tail.pervious.next to new node 
            3. set new node.previous to previous
            4. set new node.next to tail
            5. set tail.previous to new node
        '''
        current_end = self.tail.previous
        current_end.next = node
        node.previous = current_end
        node.next = self.tail
        self.tail.previous = node


    # delete node 
    def delete(self, node: ListNode):
        '''
            Delete current node by setting previous and next pointers
        '''
        node.previous.next = node.next
        node.next.previous = node.previous



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)