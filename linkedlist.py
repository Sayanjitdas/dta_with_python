"""
Linked List is a data structure where each element is a node with a value and a address pointer pointing to a next node.
Unlike a typical array it has no index and the elements are not stored adjacently in memory, it is scatterd all over the memory
but each node is linked with each other via the address pointer.
"""

class Node:

    """
    The node class used to create a node
    a node contains a value and next node pointer variable
    """
    def __init__(self,value):
        """
        constructor
        """
        self.value = value
        self.next = None # at initialize node pointer always points to nothing.


class LinkedList:

    """
    The LinkedList class which create a Linked list using node
    and it has all the required operations for a typical LinkedList
    """

    def __init__(self,value):
        """
        constructor
        """
        # creating new node
        self.node = Node(value)
        # pointing the head 
        self.head = self.node
        # pointing the tail
        self.tail = self.node
        # keeping track of the length
        self.length = 1

    def print_list(self):
        """
        This method print the values of linkedList
        """
        counter = self.head
        while counter is not None:
            print(counter.value)
            counter = counter.next

    def append(self,value):
        """
        This method adds a value with a new node at the end of the linked list
        it's time complexity --> BigO(1)
        """
        # initializing a new node
        new_node = Node(value)
        # check if linked list is empty which shall not be the case
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # adding the new node to the linked list
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        """
        This method pops/remove the tail node from linked list
        time complexity --> BigO(n)
        """
        # create counter variables post and pre
        post = self.head # this is the counter where we will get the last node
        pre = None # this is the counter where we will get 2nd last node

        # edge case where linked list has no element to pop
        if self.length == 0:
            return None

        # edge case where linked list has only one element to pop
        if self.length == 1:
            popped_value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return popped_value

        # looping through the linked list to find the 2nd last node
        while post.next is not None:
            pre = post
            post = post.next

        # re-assigning self.tail to previous node
        self.tail = pre
        # making tail node point to Nothing.
        self.tail.next = None
        # decrementing length
        self.length -= 1
        # popping out last node value
        return post.value

if __name__ == "__main__":
    new_linked_list = LinkedList(100)
    new_linked_list.append(101)
    # new_linked_list.append(102)
    new_linked_list.print_list()
    print("popped -->",new_linked_list.pop())
    print("popped -->",new_linked_list.pop())
    print("popped -->",new_linked_list.pop())
    new_linked_list.print_list()
