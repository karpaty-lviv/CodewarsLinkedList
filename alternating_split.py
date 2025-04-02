"""Alternating Split"""


class Node(object):
    """Linked List"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """Context"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Split"""
    if not head or head.next is None:
        return Context(head, head.next)
    first_head = head
    second_head = head.next
    current_node = head.next.next
    parity_check = 0
    first = first_head
    second = second_head
    while current_node is not None:
        if parity_check == 0:
            first.next = current_node
            current_node = current_node.next
            first = first.next
        if parity_check == 1:
            second.next = current_node
            current_node = current_node.next
            second = second.next
    return Context(first_head, second_head)
