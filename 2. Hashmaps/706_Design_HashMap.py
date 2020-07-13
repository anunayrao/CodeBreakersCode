class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [Node() for _ in range(self.size)]

    def find_node(self, key: int):
        index = key % self.size
        prev = self.buckets[index]
        current = prev.next

        while current is not None:
            if current.key == key:
                return prev
            prev = prev.next
            current = current.next

        return prev

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        prev = self.find_node(key)
        if prev.next is None:
            prev.next = Node(key, value)
        else:
            # update
            prev.next.value = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is None:
            return -1
        return prev.next.value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is not None:
            prev.next = prev.next.next