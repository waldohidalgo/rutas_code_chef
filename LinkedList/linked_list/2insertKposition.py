# cook your dish here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_k(self, value, k):
        new_node = Node(value)
        current = self.head
        i=0
        
        #If there are no nodes in the linked list
        #Set the new node as head and return
        if current is None:
            self.head = new_node
            return
        
        #Iterate to the k-th node

        if k==0:
            new_node.next = self.head
            self.head = new_node
            return
        while i<=k-1:
            if i==k-1:
                new_node.next, current.next = current.next, new_node
                return
            current = current.next
            i+=1
            

        # Set the next of new Node to next of current
    
        #Set the next of current to new Node



    def print_values(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())
    x, k = map(int, input().split())
    linked_list = LinkedList()
    vals = list(map(int, input().split()))
    for i in range(len(vals)):
        a = vals[i]
        linked_list.insert_after_k(a, i)
    linked_list.insert_after_k(x, k)
    linked_list.print_values()
