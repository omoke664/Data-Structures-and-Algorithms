class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        
        
    def is_empty(self):
        if self.front == -1:
            return
    
    def peek(self):
        
        if self.is_empty():
            print("Queue Underflow")
            return
        else:
            return self.queue[front]