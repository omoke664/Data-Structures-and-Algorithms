""""ALGORITHM
1. Start.
2. Create a new node and assign the data
3. Find the last node
4. Point the last node to the new node.
5. End
...."""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next: #iterate to find last node
            current = current.next
        current.next = new_node
        
    
    def listprint(self):
        val = self.head
        print("Linked List: ")
        while val is not None:
            print(val.data)
            val = val.next
            
#create a linked list
l1 = LL()

#add elements to the end
l1.append(23)
l1.append(12)
l1.append(7)
l1.append(14)
l1.append(61)

#print the linked list
l1.listprint()