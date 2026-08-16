"""We need to create a node class
Create an instance of Node
Add it to Stack by push() method
remove the nodes from Stack by pop() method"""

class Node:
    __slot__=[, 'value', 'next']

    def __init__(self, value, next):
        self.value = value 
        self.next = next

class Stack:
    __slots__ = ['top', 'size']