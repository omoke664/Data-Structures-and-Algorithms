class Stack:
    def __init__(self, max_size):
        self.arr = [None] * max_size #Create an array of specified size
        self.top = -1 # initialize the top index to -1 (empty stack)
        self.max_size = max_size
        
        
    def is_full(self):
        #checks if the stack is full
        return self.top  == self.max_size -1
    
    def push(self, data):
        #inserts an element into the stack
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.arr[self.top] = data
        print("Pushed element:" , data)
        
        
#Example usage:
stack = Stack(5) #creating a stack with max_size = 5

stack.push(10)
stack.push(20)
stack.push(30)

print(stack)
    