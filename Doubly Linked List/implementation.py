class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
            return
        new_node.next= self.head
        self.head.prev = new_node
        
    #insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next  = new_node
        
        new_node.prev = last
        
    #insert after a given node
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node can't be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next 
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            
            new_node.next.prev = new_node
            
    #delete
    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next
        
        if temp.next is None:
            return
        if temp.next.next is None:
            temp.next = None
        else:
            temp.next = temp.next.next 
            temp.next.prev = temp
            
            
        #print the list
        def print_list(self):
            temp = self.head 
            while temp:
                print(temp.data, end = " ")
                temp = temp.next