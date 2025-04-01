"""Sorted Insert"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if not head:
        return
    if data <= head.data:
        result = Node(data)
        result.next = head
        return result
    current_node = head
    while current_node.next is not None:
        if current_node.next.data < data:
            break
        current_node = current_node.next
    temp = current_node.next
    current_node.next = Node(data, temp)
    return current_node