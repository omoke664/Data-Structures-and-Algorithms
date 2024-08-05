class Stack:
    def __init__(self, max_size):
        self.arr = [None] * max_size 
        self.top = -1
        self.max_size = max_size
    def is_empty(self):
        #checks if stack is empty
        return self.top == -1
        
    def peek(self):
        #returns the top element without removing it
        if self.is_empty():
            print("Stack underflow")
            return
        return self.arr[self.top]
        