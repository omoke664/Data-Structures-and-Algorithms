class Node:
    def __init__(self, data  = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        if position < 1:
            print("Invalid position")
            return
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        prev = None
        count = 1
        
        while current and count < position:
            prev = current 
            current = current.next
            count += 1
            
        if not current:
            print("Position out of bounds")
            return
        
        prev.next = new_node
        new_node.next = current
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            
            
linked_list = LinkedList()
linked_list.insert_at_position(10, 1)
linked_list.insert_at_position(20,2)
linked_list.insert_at_position(30,1)
linked_list.print_list() #output 30 10 20