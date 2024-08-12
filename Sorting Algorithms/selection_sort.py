"""Selection Sort
selection_sort(arr) function: Defines the selection sort function that takes an array as input.
n = len(arr): Calculates the length of the array.
Outer loop: Iterates through the array from the beginning to the second-to-last element.
- i: represents the index of the currently considered element.
Inner loop: finds the minimum element in the unsorted part of the array.
- min_idx: stores the index of the minimum element found so far.
- compares each element in the unsorted part with the current minimum.
- Updates min_idx: if a smaller element is found. 

Swap: Swaps the minimum element with the first element of the unsorted part.

Time complexity: O(n^2)
Space complexity: O(1)

    
"""

def selection_sort(arr):
    
    n  = len(arr)
    
    #traverse through all array elements
    for i in range(n):
        #find the minimum element in remaining unsorted array
        min_idx = i
        for j in range( i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        #swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
#Example usage
my_array = [64, 25, 12, 22, 11, 90]

#sort the arrays
selection_sort(my_array)

print("Sorted array:", my_array)

