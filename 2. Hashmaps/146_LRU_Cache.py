
class Node:
    
    def __init__(self, key, value):
        self.key =key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node("head","head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addtoHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        
    def removefromTail(self):
        n = self.tail.prev
        k = n.key
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        n = None
        return k
        
    def deleteNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.map = {}
        self.size = 0
        

    def get(self, key: int) -> int:
        
        if key in self.map:
            node = self.map[key]
            val = node.value
            self.dll.deleteNode(node)
            del self.map[key]
            node = Node(key, val)
            self.dll.addtoHead(node)
            self.map[key] = node
            return val
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.map:
            node = self.map[key]
            self.dll.deleteNode(node)
            node = Node(key,value)
            self.map[key] = node
            self.dll.addtoHead(node)
        
        elif self.size < self.capacity:
            self.size += 1
            node = Node(key, value)
            self.map[key] = node
            self.dll.addtoHead(node)
        else:
            k = self.dll.removefromTail()
            del self.map[k]
            self.size -= 1
            self.put(key,value)
            
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
