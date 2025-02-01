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

    #printing all the values of linked list
    def print_list(self):

        #start from the head of the linked list
        temp = self.head
        
        #traversing to the list until temp becomes None(end of the list)
        while temp:
            
            print(temp.value) #printing value of current node
            temp = temp.next #move to next node
#crating instance of the class with initial value 2
my_linked_list = LinkedList(2)

#print the values in the list
print("Values of the linked list: ")
my_linked_list.print_list()
        