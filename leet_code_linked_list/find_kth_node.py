"""
LL: Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the linked list has fewer than k items, the program should return None.

The find_kth_from_end function should follow these requirements:

 - The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

 - The fast pointer should move k nodes ahead in the list.

 - If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

 - The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

 - The function should return the slow pointer, which will be at the k-th position from the end of the list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  

def find_kth_from_end(linked_list,index):

    # initializing the fast and slow counter
    fast = linked_list.head
    slow = linked_list.head
    counter = 0

    # moving the fast node k times
    while counter < index - 1:
        fast = fast.next
        counter += 1
    
    # checking if fast node is None i.e LL is shorter than k
    if fast is None:
        return None
    
    # moving the slow and fast to get the kth node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    return slow

# def find_kth_from_end(linked_list,index):

#     fast = linked_list.head
#     slow = linked_list.head

#     for _ in range(index):
#         if fast is None:
#             return None
#         fast = fast.next

#     while fast:
#         slow = slow.next
#         fast = fast.next

#     return slow
        
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
#                                             #
#    This is a separate function that is      #
#    not a method within the                  #
#    LinkedList class.                        #
#    INDENT ALL THE WAY TO THE LEFT.          #
#                                             #
###############################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 1
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

