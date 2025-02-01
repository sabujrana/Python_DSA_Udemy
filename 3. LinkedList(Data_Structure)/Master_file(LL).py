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
        while temp is not None:
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

### prepend code (adding elements to the beginning of the list)
"""
def prepend(self, value):
    new_node = Node(value)
    
    if self.length == 0:
        self.head = new_node 
        self.tail = new_node
    else:
        new_node.next = head
        self.head = new_node
    self.length += 1
    return True
    
"""
## code with all constructor, print, append and prepend function

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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    
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
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):

        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return True
    
my_linked_list1 = LinkedList(2)
my_linked_list1.append(3)
my_linked_list1.prepend(1)
my_linked_list1.print_list()

### pop first code 
"""
def pop_first(self):

    if self.length == 0:
        return None

    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
        self.tail = None
    return temp
"""

# All code upuntil pop_first

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
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

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
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #*
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    

my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.pop_first()
my_linked_list.print_list()


### get method code 

"""
def get(self, index):
    if index < 0 or index >= self.length:
        return None

    temp = self.head
    for _ in range(index):
        temp = temp.next
    return temp
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
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

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
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #*
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
        #for value to print
        # return temp.value
    
my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(4)
print(my_linked_list.get(2))

### Set value code
"""
def set_value(self, index, value):
    temp = self.head
    for i in range(index):
        temp = temp.next
        return True
    return False
    

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
            temp = temp.next #infinite loop will run if we do not update temp
        return True
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
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
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.set(2, 32)
print("Linked List after using set method")
my_linked_list.print_list()

## inserting new node in Linked list
# code 

"""
def insert(self, index, value):
    if index < 0 or index > self.length:
        return False

    if index = 0:
        return prepend(value)
    
    if index = self.length:
        return append(value)
    new_node = Node(value)
    temp = self.get(index-1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True

"""

class Node:
    def __init__(self, value):
        self.value = value #assign value 
        self.next = None 

class LinkedList:
    def __init__(self, value):
        #constructing node and added value 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head #pointing head by temp
        while temp: #checking if temp is None i.e empty list   
            print(temp.value) #printing the value by calling pointer with value
            temp = temp.next #updating pointer
        return True

    def append(self, value):
        new_node = Node(value) #adding node
        if self.length == 0: #checking for empty list
            self.head = new_node #update with new_node value in case of empty 
            self.tail = new_node
        else:
            self.tail.next = new_node #pointing tail pointer to new node 
            self.tail = new_node #pointing added new node by tail
        self.length += 1 
        return True

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
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:  # Check if the node exists
            temp.value = value
            return True
        return False  # Return False if the index is invalid

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

# Example usage:
my_linked_list = LinkedList(0)
my_linked_list.append(2)
print("Initial list:")
my_linked_list.print_list()

my_linked_list.insert(1, 3)
print("List after inserting 3 at index 1:")
my_linked_list.print_list()


## remove by index
#code 
"""
def remove(self, index):
    if index < 0 or index >= length:
        return None
    if index == 0:
        return self.pop_first()

    if index == self.length - 1:
        return self.pop()
    pre = self.get(index-1)
    temp = pre.next
    pre.next = temp.next 
    temp.next = None
    self.length -= 1
    return temp
"""
class Node:
    def __init__(self, value):
        self.value = value #assign value 
        self.next = None 

class LinkedList:
    def __init__(self, value):
        #constructing node and added value 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head #pointing head by temp
        while temp: #checking if temp is None i.e empty list   
            print(temp.value) #printing the value by calling pointer with value
            temp = temp.next #updating pointer
        return True

    def append(self, value):
        new_node = Node(value) #adding node
        if self.length == 0: #checking for empty list
            self.head = new_node #update with new_node value in case of empty 
            self.tail = new_node
        else:
            self.tail.next = new_node #pointing tail pointer to new node 
            self.tail = new_node #pointing added new node by tail
        self.length += 1 
        return True

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
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:  # Check if the node exists
            temp.value = value
            return True
        return False  # Return False if the index is invalid

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
print("initial list:")
my_linked_list.print_list()
my_linked_list.remove(2)
print("Final List:")
my_linked_list.print_list()

#Reverse of linked list

##Code

"""
def reverse(self):
    temp = self.head 
    self.head = self.tail 
    self.tai = temp
    after = temp.next
    before = None
    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after


"""

class Node:
    def __init__(self, value):
        self.value = value #assign value 
        self.next = None 

class LinkedList:
    def __init__(self, value):
        #constructing node and added value 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head #pointing head by temp
        while temp: #checking if temp is None i.e empty list   
            print(temp.value) #printing the value by calling pointer with value
            temp = temp.next #updating pointer
        return True

    def append(self, value):
        new_node = Node(value) #adding node
        if self.length == 0: #checking for empty list
            self.head = new_node #update with new_node value in case of empty 
            self.tail = new_node
        else:
            self.tail.next = new_node #pointing tail pointer to new node 
            self.tail = new_node #pointing added new node by tail
        self.length += 1 
        return True

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
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:  # Check if the node exists
            temp.value = value
            return True
        return False  # Return False if the index is invalid

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        
        if index == self.length -1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head 
        self.head = self.tail 
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("List before reverse: ")
my_linked_list.print_list()
my_linked_list.reverse()
print("List after reverse: ")
my_linked_list.print_list()
