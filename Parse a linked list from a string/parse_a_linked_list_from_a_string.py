"""Parse a linked list from a string"""


from linked_list_class import Node


def linked_list_from_string(s):
    """Make a linked list from string"""
    order = s.split(' -> ')
    if s == 'None':
        return None
    if len(order) == 1:
        return Node(order[0])
    if order[1] == 'None':
        return Node(int(order[0]))
    return Node(int(order[0]), linked_list_from_string(' -> '.join(order[1:])))
