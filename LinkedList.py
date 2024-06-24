#
from Node import Node


class LinkedList:
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

#         def __init__(self, value):
#
#         def append(self, value):
#
#         def pop(self):
#
#         def prepend(self, value):
#
#         def insert(self, index, value):
#
#         def remove(self, index):