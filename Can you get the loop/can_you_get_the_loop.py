"""Can you get the loop ?"""


class Node():
    """Class for node in linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


def loop_size(node):
    """Find loop size"""
    turtle = node
    rabit = node.next.next
    while turtle != rabit:
        turtle = turtle.next
        rabit = rabit.next.next
    counter = 1
    rabit = rabit.next
    while rabit != turtle:
        rabit = rabit.next
        counter += 1
    return counter
