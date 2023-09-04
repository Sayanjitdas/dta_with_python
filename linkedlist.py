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
    
    def prepend(self,value):

        """
        This method adds a new node at the beginning of the linked list
        Time complexity --> BigO(1)
        """
        # initializing new node
        new_node = Node(value)
        # prepend when linked list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # prepend when linked list has item in it
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pre_pop(self):

        """
        This method pops out first node from linked list
        Time complexity --> BigO(1)
        """

        # edge case where linked list empty
        if self.length == 0:
            return None
        # edge case where linked list has only one item
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp.value
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.value

    def get_value_by_index(self,index):

        """
        This method return the value of the node
        with specified index 
        Time complexity --> BigO(n)
        """
        # edge case where index is out of bound
        if index < 0 or index >= self.length:
            raise IndexError(f"{index} is out of range..")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value
    
    def set_value_by_index(self,index,value):

        """
        This method set the sepcified value in the specified index
        of the linked list.
        time complexity --> BigO(n)
        """

        # edge case where index is out of range
        if index < 0 or index >= self.length:
            raise IndexError(f"{index} is out of range..")
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value

    def insert(self,index,value):

        """
        This method insert a new node at a specified index 
        in a linked list 
        Time complexity --> BigO(n)
        """

        # edge case where index out of range
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} is out of range..")
        # edge case where index is 0 i.e the first index in the linked list
        elif index == 0:
            self.prepend(value) # best case scenario BigO(1)
        # edge case where index is last index in the linked list
        elif index == self.length - 1:
            self.append(value) # worst case scenario BigO(n)
        else:
            # creating a new node
            new_node = Node(value)
            # creating a temp variable to point to previous node of 
            # the index specified
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            # pointing the new node to existing next node
            new_node.next = temp.next
            # inserting the new node at the index
            temp.next = new_node
            # incrementing the length by 1
            self.length +=1

    def remvove(self,index):

        """
        This method removes a node from a linked list at a specified index
        Time complexity --> BigO(n)
        """

        # edge case where index out of range
        if index < 0 or index >= self.length:
            raise IndexError(f"index {index} is out of range..")
        # edge case where index is 0
        elif index == 0:
            temp = self.pre_pop() # at best case 
        # edge case where index is last index
        elif index == self.length - 1:
            temp = self.pop() # at worst case
        else:
            # grabbing the node of previous index
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            # grabbing the node to remove
            temp = prev.next
            # re assigning the next node with prev node
            prev.next = temp.next
            temp = None
            self.length -= 1

    def reverse(self):

        """
        This method reverse the linked list
        Time complexity --> BigO(n)
        """

        # swapping the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # creating two counter variable
        before = None
        after = temp
        # reversing the linked list
        for _ in range(self.length):
            after = temp.next # assign the next node
            temp.next = before # reversing the link of the node
            # shifting the counter
            before = temp
            temp = after


if __name__ == "__main__":
    new_linked_list = LinkedList(100)
    new_linked_list.append(101)
    new_linked_list.append(102)
    # new_linked_list.print_list()
    # print("popped -->",new_linked_list.pop())
    # print("popped -->",new_linked_list.pop())
    # print("popped -->",new_linked_list.pop())
    # print("---------------------")
    # new_linked_list.prepend(99)
    # new_linked_list.print_list()
    # print("---------------------")
    # new_linked_list.pre_pop()
    # new_linked_list.print_list()
    # print(new_linked_list.get_value_by_index(2))
    # new_linked_list.set_value_by_index(2,200)
    # new_linked_list.print_list()
    # new_linked_list.insert(1,500)
    # new_linked_list.print_list()
    # new_linked_list.remvove(1)
    # new_linked_list.print_list()
    new_linked_list.print_list()
    print("after reverse..")
    new_linked_list.reverse()
    new_linked_list.print_list()