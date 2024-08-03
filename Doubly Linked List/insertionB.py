class Node:
    def __init__(self, data):
        #represents a node in the doubly linked list.
        
        #Args:
            # data: the data to be stored in the node.
        self.data = data
        self.prev = None #pointer to the previous node
        self.next = None #pointer to the next node
        
class DoublyLinkedList:
    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.head = None #Head of the list.
        
        #inserts a new node at the beginning of the list.
        def insert_at_beginning(self, data):
            
            #args:
                #data: the data to be inserted.
            new_node = Node(data)
            
            #if the list is empty, the new node becomes the head.
            if self.head is None:
                self.head = new_node
                return
            #otherwise, adjust the pointers
            new_node.next = self.head #set the next pointer of the new node to the current head
            self.head.prev = new_node #set the previous pointer of the current head to the new node.
            self.head = new_node #update the head to pont to the new node.
            
            