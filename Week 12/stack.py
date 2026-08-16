class Node:

    _slots_=["next","value"]
    
    def _init_(self,next=None,value=0):
        self.next=next 
        self.value=value 

    def get_next(self):
        return self.next 

    def get_value(self):
        return self.value 

    def print_node(node_sequence):
        if node_sequence is None:
            return
        print(node_sequence, end="," if node_sequence is not None else "")
        print_node(node_sequence.next)

class Stack:

    _slots_=["top","size"]

    def _init_(self):
        self.top= None 
        self.size==0
    
    def is_empty(self):
        return self.size == 0 
    
    def get_size(self):
        return self.size 
    
    def push(self, value):
        new_node=Node(next=self.top, value=value)
        self.size=self.size+1
    
    def pop(self):
        if self.is_empty():
            raise IndexError ("Pop from an empty stack")