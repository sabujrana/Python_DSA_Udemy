########## Coding Exercise ##########

"""
LL: Constructor
You are tasked with implementing a basic data structure: a singly linked list.

To accomplish this, you will create two classes, Node and LinkedList.

The Node class will represent an individual node within the linked list, while the LinkedList class will manage the overall list structure.

Your implementation should satisfy the following requirements:



Create a Node class with the following features:

A constructor that takes a value as an argument and initializes the value attribute of the node.

A next attribute, initialized to None, which will store a reference to the next node in the list.

Create a LinkedList class with the following features:

A constructor that takes a value as an argument, creates a new Node with that value, and initializes the head and tail attributes of the linked list to point to the new node.

A length attribute, initialized to 1, which represents the current number of nodes in the list
"""


#Define the node class
class Node: 
    

    def __init__(self, value):
        self.value = value #Each node holds a value
        self.next = None #Each node has pointer to next node, initially set to None
    
class LinkedList:

    #__init__ method initialize linked list with single node
    def __init__(self, value):

        #Creating node with given value
        new_node = Node(value)

        #Set the head of the linked list to point to new node
        self.head = new_node

        #Set the tail of the linked list ot point to new node
        self.tail = new_node

        # Initialize the length of the linked list to 1 (since it has one node)
        self.length = 1

# Create an instance of the LinkedList class with an initial value of 4
my_linked_list = LinkedList(4)

#print the value of the head node
print("Head value = ",my_linked_list.head.value)

#print the value of the tail node
print("Tail value = ",my_linked_list.tail.value)

#print the length of the linked list
print("Length = ",my_linked_list.length)



"""
Concerned question:
(1) what are the difference between value in Node class and LinkedList class? 

-> value in Node class is attribute which stores actual data for single node. Each node in Linked List holds piece of data of any type and stored in "value" attribute. 
Also it is instance of Node class.
node1 = Node(2)
node2 = Node(4)

-> value in LinkedList class is parameter to pass inside init method while creating linked list. It is used to initialize first node of the list but not stored as in attribute. 

--> Node class is responsidble for storing data(value) and linking to next node(next).
--> Linked List is responsible for managing overall structure of the list. 

"""


 
#Define the class node
class Node: 
    
    def __init__(self, value):
        self.value = value # Each node holds a value
        self.next = None # Each node has a pointer to the next node, initially set to None

# Define the LinkedList class
class LinkedList:
    
    def __init__(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        
        # Set the head of the linked list to point to new node
        self.head = new_node

        # Set the tail of the linked list to point to new node
        self.tail = new_node

        # Initialize length of linked list to 1(since it has one node)
        self.length = 1

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    