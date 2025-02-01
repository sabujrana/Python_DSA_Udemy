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