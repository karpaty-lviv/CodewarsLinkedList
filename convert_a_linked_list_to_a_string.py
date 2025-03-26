"""Convert a linked list to a string"""


from linked_list_class import Node


def stringify(node):
    """Returns string represantation of linked list"""
    if node is None:
        return 'None'
    text = f'{node.data}'
    current_node = node.next
    while current_node.next is not None:
        text += f' -> {current_node.data}'
        current_node = current_node.next
    text += f' -> {current_node.data} -> None'
    return text
