########## Coding Exercise ##########

"""
LL: Append
Implement the append method for the LinkedList class.

The append method should add a new node with a given value to the end of the linked list, updating the tail attribute and the length attribute accordingly.



Keep in mind the following requirements:



The method should handle the cases where the list is empty and where the list already has one or more nodes.

The method should create a new node with the given value and add it to the end of the list.

The method should update the tail attribute of the LinkedList correctly.

The method should update the length attribute of the LinkedList to reflect the addition of the new node
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
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        

        
        
        #################################
        # FINISH WRITING APPEND METHOD  #
        # INSERT IF/ELSE STATEMENT HERE #
        #################################
    #method to append a new node to the end of linked list
    def append(self, value):
        # Create new node with given value
        new_node = Node(value)

        # Check if the linked list is empty
        if self.length == 0:
            #If empty set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # If not empty, add new node after the current tail
            self.tail.next = new_node
            # Update tail to point to new node
            self.tail = new_node 
        # Increase length of the linked list by 1       
        self.length += 1
        
        # Return True indicate success
        return True




my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""


