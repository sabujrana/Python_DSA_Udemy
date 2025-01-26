#cookie class having 2 function
class Cookie: 
    
    def __init__(self, color): #constructor
        self.color = color #apply for specific instance
    
    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color
# creating 2 new cookies
cookie_one = Cookie('green')

cookie_two = Cookie('Blue')

#print statement
print("Cookie one is: ", cookie_one.get_color())
print("Cookie two is: ", cookie_two.get_color())

cookie_one.set_color("yellow") #calling set_color function

print("Cookie one is now: ", cookie_one.get_color())
print("Cookie two is still: ", cookie_two.get_color())


### Linkedlist
class LinkedList:
    
    def __init__(self, value):
        pass

    def append(self,value):
        pass

    def pop(self):
        pass

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

a = LinkedList()