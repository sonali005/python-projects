class Node:

    __slots__ = ["next", "value"]

    def __init__ (self, next = None, value = 0):
        self.next = next
        self.value = value
    
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value
    
    def print_node(node_seq):
        if node_seq is None:
            return 
        print(node_seq.value, end= "," if node_seq.next is not None else "")
        print_node(node_seq.next)

        
