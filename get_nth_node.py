"""Get Nth Node"""


from linked_list_class import Node


def get_nth(node, index):
    result = node
    for _ in range(index):
        result = result.next
    return result

