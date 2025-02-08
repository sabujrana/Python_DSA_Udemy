########## Coding Exercise ##########
"""
LL: Pop
Your task is to implement the pop method for the LinkedList class.

The pop method should remove the last node (tail) from the linked list and return the removed node. If the list is empty, the method should return None.

After the last node is removed, the second-to-last node should become the new tail of the list.

Additionally, if the list becomes empty after the pop operation, both the head and tail attributes should be set to None.



Keep in mind the following requirements:



The method should handle the cases where the list is empty, has only one node, or has multiple nodes.

The method should update the tail attribute of the LinkedList correctly.

The method should update the length attribute of the LinkedList to reflect the removal of the node.

The method should either return the removed node or None if the list is empty.


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
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
        
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

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
    # Method to remove last node from linked list
    def pop(self):
        # Check if linked list is empty
        if self.length == 0:
            return None # If empty, return None
        #Intialize two pointers: pre(previous) and temp(temporary)          
        pre = self.head 
        temp = self.head
        # Traverse the list until temp reaches the last node
        while temp.next:
            pre = temp # Move pre to the current node
            temp = temp.next # move temp to the next node
        #After the loop, temp is the last node and pre is the second-to-last

        self.tail = pre # Update the tail to be the second-to-last node
        self.tail.next = None # Remove the reference to the last node
        self.length -= 1 # Decrease the length of the linked list by 1

        #If the list is now empty, reset head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        # Return the removed node
        return temp

 
##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")


