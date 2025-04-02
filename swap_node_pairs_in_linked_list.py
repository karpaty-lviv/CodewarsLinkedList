"""Swap Node Pairs In Linked List"""


class Node:
    """Class for linked list"""
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    """Swap pairs"""
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    while head and head.next:
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        if prev:
            prev.next = second
        prev = first
        head = first.next
    return new_head
