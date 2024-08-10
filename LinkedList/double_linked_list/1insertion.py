class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtIndex(self, index, value):
        new_node = Node(value)

        if index == 0:
            # To insert at head, make this new node the head
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            # To insert at any other position
            # Find the nodes between which we want to insert
            # By traversing from head to index - 1 position
            iter = self.head
            for _ in range(index - 1):
                iter = iter.next

            A = iter
            B = iter.next

            # Update pointers to insert newNode between A and B
            A.next = new_node
            if B:
                B.prev = new_node

            # Update pointers of newNode
            new_node.next = B
            new_node.prev = A

    def printValues(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())

    ll = LinkedList()
    val = list(map(int, input().split()))
    for i in range(len(val)):
        ll.insertAtIndex(i, val[i])

    ll.printValues()
