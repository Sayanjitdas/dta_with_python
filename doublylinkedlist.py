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


    def append(self,value):
        """ DLL is same as LL but with another node link to 
        prevoius node
        Time complexity --> BigO(1)
        Args:
            value : value of the node
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList(400)
    dll.append(101)
    dll.print_list()