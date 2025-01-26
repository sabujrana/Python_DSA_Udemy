#Integers are immutable i.e. integer value can't be changed
num1 = 11

num2 = num1

print("Before num2 value is updated: ")

print("num1 = ", num1)
print("num2 = ", num2)

print("num1 points to: ", id(num1)) #id will give the address of number stored
print("num2 points to: ", id(num2))


#Update the value of num2 
num2 = 22
print("After num2 value is updated")
print("num1 = ", num1)
print("num2 = ", num2)

print("Num1 points to: ", id(num1))
print("num2 points to: ", id(num2))

#Dictionary

dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("dict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

#updating dict2 value
dict2["value"] = 22

print("After value is updated")
print("dict1 = ", dict1)
print("dict2 = ", dict2)

print("dict1 points to: ", id(dict1))
print("dict2 points to: ", id(dict2))

#Value and addresses are changed(updated value and address shows)
#Dictionary is Mutable i.e. we can change it

##Garbage collection; if there is no variable to point(store) it will remove the value
