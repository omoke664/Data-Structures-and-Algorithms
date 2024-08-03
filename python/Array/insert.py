def insert(arr, element):
    arr.append(element)
    
if __name__ == '__main__':
    LA = [0,0,0]
    x = 0
    #array before inserting an element
    print("Array before inserting an element:")
    for x in range(len(LA)):
        print("LA", [x],  "=" , LA[x])
    print("Inserting elements....")
    #array after inserting an element
    for x in range(len(LA)):
        LA.append(x)
        LA[x] = x + 1
    print("Array after inserting elements:")
    for x in range(len(LA)):
        print("LA", [x], "=" , LA[x])
    
        