#bubble sort


def bubble_sort(arr):
 #outer loop to iterate through the list n times
 for n in range(len(arr) -1, 0, -1):
    swapped = False
    #inner loop to compare adjacent elements
    for i in range(n):
         if arr[i] > arr[i + 1]:
         #swap elements if they are in the wrong order
            swapped = True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    if not swapped:
        return
    
arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
bubble_sort(arr)
print(arr)   
