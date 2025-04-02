"""Remove Duplicate"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Node({self.data}, {str(self.next)})'

def remove_duplicates(head):
    """Remove duplicate"""
    if head is None:
        return None
    current_node = head
    while current_node.next is not None:
        if current_node.data == current_node.next.data:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head

print(remove_duplicates(Node(1, Node(2, Node(2, Node(3, Node(3, Node(4, Node(5)))))))))
