"""Parse a linked list from a string"""


from linked_list_class import Node


def linked_list_from_string(s):
    """Make a linked list from string"""
    order = s.split(' -> ')
    if len(order) == 1:
        return Node(order[0])
    if order[1] == 'None':
        return Node(int(order[0]))
    return Node(order[0], linked_list_from_string(' -> '.join(order[1:])))


def stringify(node):
    """Returns string represantation of linked list"""
    if node is None:
        return 'None'
    text = f'{node.data}'
    if node.next is None:
        return f'{text} -> None'
    current_node = node.next
    while current_node.next is not None:
        text += f' -> {current_node.data}'
        current_node = current_node.next
    text += f' -> {current_node.data} -> None'
    return text


print(stringify(linked_list_from_string("1 -> 2 -> 3 -> None")))
