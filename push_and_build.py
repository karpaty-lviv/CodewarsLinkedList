"""Push & BuildOneTwoThree"""


from linked_list_class import Node


def push(head, data):
    """Push"""
    if head is None:
        return Node(data)
    linkd_lst = Node(data)
    linkd_lst.next = head
    return linkd_lst

def build_one_two_three():
    """1, 2, 3"""
    node = Node(1)
    node1 = Node(2)
    node1.next = Node(3)
    node.next = node1
    return node
