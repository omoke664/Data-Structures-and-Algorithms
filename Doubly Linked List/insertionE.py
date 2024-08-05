class Node:
    def __init__(self, data):
        #creates a new node with the given data.
        """_summary_

        Args:
            data (_type_): _description_
        """
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, data):
        #inserts a new node with the given data at the end of the line.
        """_summary_

        Args:
            data (_type_): _description_
        """
        new_node = Node(data) #creates a new node
        
        if self.head is None: #if the list is empty
            self.head = new_node #make the new node the head
            return
        #find the last node in the list
        last = self.head
        while last.next:
            last = last.next
        #link the new node to the last node
        last.next= new_node
        new_node.prev = last
        
        
    def print_list(self):
        """prints the data of all the nodes in the list
        """
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next