
LA  = [1,3,5,7,8]

#before updating
print("The original array elements are:")
for x in range(len(LA)):
    print("LA", [x], "=", LA[x])
    
#after updating
LA[2] = 10
print("The array elements after updating are: ")
for x in range(len(LA)):
    print("LA", [x], "=", LA[x])