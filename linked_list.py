class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node

    def __str__(self):
        node = linked_list.root
        s = ''
        while node:
            if s:
                s += '->'
            s += str(node.value)
            node = node.next
        return s


if __name__ == "__main__":
    linked_list = LinkedList(range(10))
    print(linked_list)
