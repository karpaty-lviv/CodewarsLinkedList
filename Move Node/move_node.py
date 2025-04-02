"""Move node"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    """Move node"""
    if source is None:
        raise Exception
    first_node = source.data
    source = source.next
    new_dest = Node(first_node)
    new_dest.next = dest
    return Context(source, new_dest)