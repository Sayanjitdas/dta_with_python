"""
LL: Partition List ( ** Interview Question)

You are given a singly linked list implementation in Python that does not have a tail pointer (which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and partition the linked list such that all nodes with values less than x come before nodes with values greater than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made up of the original nodes from the linked list that is being partitioned, one for nodes less than x and one for nodes greater than or equal to x.  None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the partitioning process).

You should then traverse the original linked list and append each node to the appropriate new linked list.

Finally, you should connect the two new linked lists together.

Let's consider the list 2 -> 8 -> 1 -> 4 -> 3 -> 7, and we'll partition around the value 4.

Before

2 -> 8 -> 1 -> 4 -> 3 -> 7

After

After calling the partition_list(4), we have:

2 -> 1 -> 3 -> 8 -> 4 -> 7


Explanation:

The partition_list method separates the nodes into two lists, one for nodes with values less than x and the other for nodes with values equal to or greater than x. The function then concatenates these two lists.

In the above example, the nodes with values less than 4 (i.e., 2, 1, and 3) come before the nodes with values equal to or greater than 4 (i.e., 8, 4, and 7).  The relative order of the nodes is preserved.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def partition_list(self,value):

        temp = self.head
        # initializing two new linked list 
        smaller_list = LinkedList(None)
        bigger_list = LinkedList(None)

        # making the head and tail None and length 0
        smaller_list.make_empty()
        bigger_list.make_empty()
        
        # traversing original linked list to partition nodes 
        for _ in range(self.length):
            if temp.value < value:
                smaller_list.append(temp.value)
            else:
                bigger_list.append(temp.value)
            
            temp = temp.next

        # making the head and tail None and length 0 for original LL
        self.make_empty()

        # appending the partitioned LLs to orginal LL
        temp = smaller_list.head
        for _ in range(smaller_list.length):
            self.append(temp.value)
            temp = temp.next
        
        temp = bigger_list.head
        for _ in range(bigger_list.length):
            self.append(temp.value)
            temp = temp.next
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
