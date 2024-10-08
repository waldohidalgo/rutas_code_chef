class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head

    def solveJosephus(self):
        #Complete this function
        c=self.head
        while c.next != c:
            c.next=c.next.next
            c=c.next
        return c.value
        


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())

        ll = LinkedList()
        for i in range(1, n + 1):
            ll.insertAtEnd(i)
        print(ll.solveJosephus())
