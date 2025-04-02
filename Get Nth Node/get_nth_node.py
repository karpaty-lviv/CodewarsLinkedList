"""Get Nth Node"""


from linked_list_class import Node


def get_nth(node, index):
    """Get nth node"""
    result = node
    if index < 0:
        raise Exception
    if result is None:
            raise Exception
    for _ in range(index):
        result = result.next
        if result is None:
            raise Exception
    return result
