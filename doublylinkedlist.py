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
        else:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1

        return node
    
    def prepend(self,value):
        """DLL prepend work similar to LL prepend
        only you have to point the prev of the next node to new node
        Time complexity --> BigO(1) 
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            temp.prev = self.head
            self.length +=1
            
    def pop_first(self):
        """Identical to LL 
        Time complexity --> BigO(1)
        Raises:
            ValueError: When DLL is empty

        Returns:
            node
        """

        if self.head is None:
            raise ValueError("DLL is empty")
        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
        else:
            node = self.head
            self.head = node.next
            self.head.prev = None
            self.length -= 1
        return node
    
    def get_value_by_index(self,index):
        """Similar to LL but only optimization is
        we can search either of the end head or tail
        depending on the index number and size of the length.
        Time complexity --> BigO(n)
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range for DLL..")
        if index < self.length/2:
            # will search on first half of the DLL
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            # will search on second half of the DLL
            temp = self.tail
            for _ in range(self.length - 1,index, -1):
                temp = temp.prev
            return temp

    def set_value_by_index(self,index,value):
        """
        same as LL
        Time complexity --> BigO(n)
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range for DLL..")
        else:
            node = self.get_value_by_index(index)
            node.value = value


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList(400)
    dll.append(101)
    dll.append(201)
    dll.prepend(99)
    # print(dll.pop().value)
    # print(dll.pop().value)
    # print(dll.pop_first().value)
    print(dll.set_value_by_index(2,500))
    dll.print_list()