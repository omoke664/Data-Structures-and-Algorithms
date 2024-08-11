"""PSEUDOCODE:
    enqueue(queue, data):
    if is_full(queue):
        return "Queue overflow"
    else:
        rear = (rear + 1) % capacity #Circular queue handling
        queue[rear] = data
        return "Success"
"""

class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity #create a list to store elements
        self.front = self.rear = -1 #initialize front and rear pointers
        self.capacity = capacity
        
    def is_full(self): #check if the queue is full
        return self.rear == self.capacity -1 #returns true is the queue is full, false othewise
    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow")
        else:
            if self.rear == -1: #if the queue is empty
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity #circular queue handling
            self.queue[self.rear] = item
            print(item, "Enqueued to queue")