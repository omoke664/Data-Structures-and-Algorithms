class Stack:
    def __init__(self, max_size):
        self.arr = [None] * max_size
        self.top = -1
        self.max_size = max_size
        
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.max_size -1
    
    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = data
        print("Pushed element:", data)
        
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return
        data = self.arr[self.top]
        self.top -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            print("Stack Underflow")
            return
        return self.arr[self.top]
    
    def print_stack(self):
        if self.is_empty():
            print("Stack Underflow")
            return
        for i in range(self.top + 1):
            print(self.arr[i], end = "")
            print(" ")
        print()
        
        
        
#Example Usage
stack = Stack(5)


#pushing elements to the stack
stack.push(12)
stack.push(53)
stack.push(27)
stack.push(32)
stack.push(97)

#looking at the top element
print("Top Element:",stack.peek())

#removing the top element
element = stack.pop()
print("Popped Element:", element)

#displaying elements already in the stack
stack.print_stack() 

