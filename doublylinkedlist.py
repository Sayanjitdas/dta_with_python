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
        """ DLL append is same as LL but with another node link to 
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

    def pop(self):
        """DLL pop is a bit different than LL, we don't have to iterate
        through the List to find the node to pop cause DLL has prev link
        so we can use it to pop and move the tail node
        Time complexity --> BigO(1)
        """
        if self.head is None:
            raise ValueError("DLL is empty!!")
        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
            return node


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList(400)
    dll.append(101)
    print(dll.pop().value)
    # print(dll.pop().value)
    dll.print_list()