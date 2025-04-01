"""Module for linked list"""

class Node():
    """Class for node in linked list"""
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f'Node({self.data}, {str(self.next)})'
