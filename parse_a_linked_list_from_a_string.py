"""Parse a linked list from a string"""


from linked_list_class import Node


def linked_list_from_string(s):
    """Make a linked list from string"""
    order = s.split(' -> ')
    if order[1] == 'None':
        return Node(int(order[0]))
    return Node(order[0], linked_list_from_string(' -> '.join(order[1:])))

print(linked_list_from_string("1 -> 2 -> 3 -> None"))
