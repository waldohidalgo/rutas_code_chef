class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        # Create the Node tail
        self.tail = None

    def insert_at_end(self, value):
        new_node = Node(value)
        # If there are no nodes in the linked list
        # Set the new node as head and return
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        # Set next of tail to the new Node
        self.tail.next = new_node
        
        # Set new Node as the new tail
        self.tail = new_node
        