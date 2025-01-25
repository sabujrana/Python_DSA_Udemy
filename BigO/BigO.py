"""
<> Big O: O(n)
Implement a Python function called print_items.

This function should take a single integer as an argument and print out a sequence of numbers from 0 up to, but not including, the provided integer.

The function should use a for loop and Python's built-in range function to generate the sequence of numbers.

The function signature should be: def print_items(n):


Example:

Here is an example of how your function should behave:


If you call print_items(10), your function should print:

0
1
2
3
4
5
6
7
8
9
"""
def print_items(n):
    for i in range(n):
        print(i)


print_items(10)

"""
Drop Constant:
n+n = 2n means passing n no of operations multiple times and dropping whatever constant having with n
That means adding loop/no of operations every time
"""
# Example
def show_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)
show_items(10)