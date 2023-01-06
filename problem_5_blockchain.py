import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data.encode("utf-8")
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return str(self.hash)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class Blockchain:
    def __init__(self, init_list=None):
        self.head = None
        self.size = 0
        if init_list:
            for value in init_list:
                self.append(value)

    def __len__(self):
        return self.size

    def append(self, block: Block):
        if self.head is None:
            self.head = Node(block)
            self.size += 1
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(block)
        self.size += 1
        return

    def search(self, block: Block):
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == block:
                return node
            node = node.next

        return "Value not found in the list."


blockchain = Blockchain()

# Test Case #1 - Add a Block
block = Block(
    timestamp=datetime.now(),
    data="something that goes here".encode("utf-8"),
    previous_hash=len(blockchain),
)

assert len(blockchain) == 0
blockchain.append(block)
assert len(blockchain) == 1

# Test Case #2 - Look for a block
block = Block(
    timestamp=datetime.now(),
    data="first thing goes here".encode("utf-8"),
    previous_hash=len(blockchain),
)

blockchain.append(block)

assert str(blockchain.search(block)) == block.hash

# Test Case #3 - Look for a non valid node
block = Block(
    timestamp=datetime.now(),
    data="something that goes here".encode("utf-8"),
    previous_hash=len(blockchain),
)

assert blockchain.search(block) == "Value not found in the list."
