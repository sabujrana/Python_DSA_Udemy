## Differences between Linked list and List in python

#1 Linked list doesn't have index like list in python. 
#2. List is contagious place in memory. i.e. they are always next to each other.
#3. Linked list have head(points to first node), tail(point to last item) and each node points to next and the last node will points to None
#4. Linked list is non-contagious

###LL: Big(O) #appending or inserting to end

# LL: Under the hood
#similar like nested dictionary 


head = {
    'value': 11,
    'next': {
        'value' : 3, 
        'next': {
            'value': 23, 
            'next': {
                'value': 7,
                'next': None
                }

                }

            }
        }

print(head['next']['next']['value'])

## Only runs with linked list
# print(my_linked_list.head.next.next.value)

## LL: constructor

"""
class LinkedList: 
    def __init(self, value):
        pass #create node i.e. initialize new linked list
    def append(self, value):
        pass #create node and add node to the end
    
    def prepend(self, value):
        pass #create new node and add Node to beginning
    def insert(self, index, value):
        pass #create new node and insert a node

1. We pass value to all of those above function
2. All of those above function creates a node and pass value
3. Instead of that we can create single class for node
4. Node is having value and next, when we have value that apply to specific instance we use self keyword

class Node:
    
    def __init__(self, value):
        self. value = value
        self.next = None
class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

"""
##LL: Constructor code 
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
"""
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

A length attribute, initialized to 1, which represents the current number of nodes in the list.




"""
# Soltuion:
class Node: 
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
    
    def __init__(self, value): 
        new_node = Node(value) #create first node with this which calls Node class
        self.head = new_node #points to head
        self.tail = new_node #points to tail
        self.length = 1 #keep tracking of link

my_linked_list = LinkedList(4) #initiate linked list constructor init of LinkedList class

print("Head value = ",my_linked_list.head.value) #print value
print("Tail value = ",my_linked_list.tail.value)
print("Length = ",my_linked_list.length)


###LL: print code 

"""
def print_code(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next
"""


### LL: append 
"""
def append(self, value):
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length +=1
    return 1
"""       
### Combined code of constructor with print function and append 

class Node: 

    def __init__(self, value):
        self. value = value
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
            temp = temp.next #**

    def append(self, value):
        new_node = Node(value)
        if self.length == 0: #**
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node #**
        self.length += 1

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.print_list()
            
##Pop code
"""
def pop(self):
    if self.length == 0:
        return None
    temp = self.head
    pre = self.head
    while temp.next: #that means temp.next is not Nonen
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
        self.head = None
        self.tail = None
    return temp

"""

#Full code till pop

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
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):

        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = 0
            self.tail = 0
        return temp
        # return temp.value #to check te poped value

my_linked_list = LinkedList(2)
my_linked_list.append(3)

#printing the list

# my_linked_list.print_list()

#2 items - returns 2 nodes
print(my_linked_list.pop())

#1 items - returns 1 nodes
print(my_linked_list.pop())

#0 items - returns None
print(my_linked_list.pop())







