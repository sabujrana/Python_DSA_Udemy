########## Coding Exercise ##########

"""
Implement a method print_list(self) that prints the linked list's elements, one per line.
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

    # Method to print all vlues in linked list
    def print_list(self):
        temp = self.head # Start at the head of the linked list
        while temp: # Traverse the list until temp becomes None(end of node)
            print(temp.value) # Print the value of current node
            temp = temp.next # Move to the next node
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    
"""
