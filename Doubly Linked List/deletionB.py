class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev= None
        
        
class DoublyLinkedList:
    def __init__(self):
        
        self.head = None
        
    def delete_at_beginnig(self):
        #check if list is empty
        if self.head is None:
            print("List is empty")
            return
        
        #store the head node in a temporary variable
        temp = self.head
        
        #make the next node the new head
        self.head = temp.next
        
        #update the previous Pointer of the new head
        if self.head:
            self.head.prev = None
            
        #delete the old head
        del temp
        
        
    def print_list(self):
        
        temp = self.head
        while temp:
            print(temp.data, end= " ")
            temp = temp.next