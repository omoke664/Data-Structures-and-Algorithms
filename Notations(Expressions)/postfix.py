def evaluate_postfix(expression):
    stack = [] #Initializing an empty stack
    
    #scan the expression from left to right
    for char in expression:
        if char.isdigit():
            #if it is an operand, push it to the stack
            stack.append(int(char))
        else:
            #it it is an operator, pull operands from the stack and perform the operation
            op2 = stack.pop() #pop the top operand
            op1 = stack.pop() #pop the next operand
            
            
            #perform the operation based on the operator
            if char == '+':
                result = op1 + op2
                
            elif char == '-':
                result = op1 - op2
                
            elif char == '*':
                result = op1 * op2
                
            elif char == '/':
                result = op1 /op2
            else:
                raise ValueError(f"Unsupported operator: {char}")
            
            #store the result back to the stack
            stack.append(result)
            
        #the final result should be the only element left in the stack    
        return stack.pop()
            
            
#Example usage
expression = "231*+9-"
result = evaluate_postfix(expression)

print(f"Result using Postfix Expression is: {result}")    
    
    