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
        while temp:
            print(temp.value)
            temp = temp.next

        return True

    # add new node to the end of linked list
    def append(self, value):

        new_node = Node(value) #create new node with given value
        
        if self.length == 0: #check if the linked list is empty
            #if empty, set both head and tail to new node
            self.head = new_node 
            self.tail = new_node
        else:
            #if not empty, set new node after the current tail
            self.tail.next = new_node
            #update tail to point to new node
            self.tail = new_node
        #increase the length of linked list by 1
        self.length += 1

        return True
    
my_linked_list = LinkedList(11)
print("Linked list before append:")
my_linked_list.print_list()

my_linked_list.append(7)
print("Linked list after append")
my_linked_list.print_list()

