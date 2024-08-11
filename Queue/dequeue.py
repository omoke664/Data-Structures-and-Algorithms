"""if is_empty(queue):
        return "Queue Underflow"
        else:
            data = queue[front]
            if front == rear:
                front = rear = -1 #if only one element
            else:
                front = (front + 1) % capacity #circular motion handling
            return data
            
    """
    
class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.capacity = capacity
        
        
    def is_empty(self):
        return self.front == -1 #returns true is queue is empty , False Otherwise
    
    def dequeue(self):
        if self.is_empty():
            print ("Queue Underflow")
            return
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1 #if only one element
            else:
                self.front = (self.front + 1) % self.capacity #circular queue handling
            return data
    