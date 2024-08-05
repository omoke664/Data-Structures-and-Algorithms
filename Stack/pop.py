class Stack:
    def __init__(self, max_size):
        self.arr = [None] * max_size #create an array of specified size
        self.top = -1 #initialize the top index to -1 (empty stack)
        self.max_size = max_size
        
    def is_empty(self):
            #checks if stack is empty
            return self.top == -1
        
    def pop(self):
            #removes and returns the top element from the stack            
            if self.is_empty():
                print("Stack Underflow")
                return
            data = self.arr[self.top]
            self.top -= 1
            return data
        
        
        
element = Stack.pop()
print("Popped element:", element)