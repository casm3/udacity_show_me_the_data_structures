class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList):
    # Your Solution Here
    set_1, set_2 = set_maker(llist_1, llist_2)
    set_union = set_1.union(set_2)
    return linked_list_maker(set_union)


def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1, set_2 = set_maker(llist_1, llist_2)
    set_intersection = set_1.intersection(set_2)
    return linked_list_maker(set_intersection)


def linked_list_maker(set_):
    new_linked_list = LinkedList()
    for i in set_:
        new_linked_list.append(i)

    return new_linked_list


def set_maker(llist_1, llist_2):
    set_1, set_2 = set(), set()

    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next

    return (set_1, set_2)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases

# Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3, 4]
element_2 = [5, 6]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

linked_list = union(linked_list_1, linked_list_2)

for element in ["1", "2", "3", "4", "5", "6"]:
    assert element in str(linked_list)

# Test Case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3, 4]
element_2 = [3, 4]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

linked_list = intersection(linked_list_1, linked_list_2)

for element in ["3", "4"]:
    assert element in str(linked_list)

for element in ["1", "2"]:
    assert element not in str(linked_list)

# Test Case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3, 4]
element_2 = [5, 6, 7, 8]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

linked_list = intersection(linked_list_1, linked_list_2)

assert not str(linked_list)
