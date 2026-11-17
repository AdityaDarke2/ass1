class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        curr = self.table[idx]
        while curr is not None:                     # Check duplicate keys
            if curr.key == key:
                curr.value = value                  # Update existing
                return
            curr = curr.next
        new_node = HashNode(key, value)             # Insert at head of chain
        new_node.next = self.table[idx]
        self.table[idx] = new_node

    def search(self, key):
        idx = self.hash_func(key)
        curr = self.table[idx]
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def delete(self, key):
        idx = self.hash_func(key)
        curr = self.table[idx]
        prev = None
        while curr is not None:
            if curr.key == key:
                if prev is None:
                    self.table[idx] = curr.next
                else:
                    prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            curr = self.table[i]
            while curr:
                print(f"[{curr.key}: {curr.value}]", end=" -> ")
                curr = curr.next
            print("None")
