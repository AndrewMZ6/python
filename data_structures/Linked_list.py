class Node:
    """
    instances of this class are elements 0f linked list
    """

    def __init__(self, value):
        self.data = value
        self.next = None


class linkedList:
    """
    Graphically this class looks like recursive rectangular.
    See Wiki -> linked list
    """

    def __init__(self):
        self.head = None

    def add_item_end(self, value):
        new_node = Node(value)
        curr = self.head
        if curr is None:
            self.head = new_node
            return

        while curr.next:
            curr = curr.next
        curr.next = new_node

    def add_front(self, value):
        new_node = Node(value)
        curr = self.head
        new_node.next = curr
        self.head = new_node

    def add_after(self, value, node):
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def show(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


l = linkedList()
l.add_item_end(41)
l.add_front(77)
l.add_after(85, l.head.next)
l.add_after(9, l.head.next)
l.show()
