"""
doubly linked list module
which behave same as linked list but has an extra parmeter to the node
each node keep the address of the next node as well as previous node    
"""

class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"

class DoublyLinkedList:

    def __init__(self,value):
        self.node = Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList(400)
    dll.print_list()