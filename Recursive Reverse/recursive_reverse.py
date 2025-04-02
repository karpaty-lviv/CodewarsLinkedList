"""Recursive reverse"""


class Node(object):
    """Linked list"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, prev=None):
    """Reverse"""
    if head is None:
        return prev
    next_node = head.next
    head.next = prev
    return reverse(next_node, head)
