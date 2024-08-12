"""
Import necessary libraries: No external libraries are required for this implementation.
Define the insertion_sort function: 
- takes an unsorted array as input.
- iterates through the array starting from the second element.
- stores the current element as key.
- compares the key with elements in the sorted part of the array.
- shifts elements greater than key one position ahead.
- inserts into its correct position.
- returns the sorted array.
create an example array: An unsorted my_array is created.
Call the insertion_sort function: the insertion_sort function is called with my_array as input and the result is stored in sorted_array.
Print the sorted array.
"""

#insertion sort


def insertion_sort(arr):
    
    #iterate through the array starting from the second element
    for i in range(1, len(arr)):
        #store the current element as the key
        key = arr[i]
        #initialize index for comparison
        j = i - 1
        
        #move elements greater than the key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            i -= 1
            
            #insert the key into its correct position
            arr[j + 1] = key
        
    return arr

#Example Usage:
my_array = [3,8,2,1,5,4,9,6,7]
sorted_array = insertion_sort(my_array)

#print the sorted array
print(sorted_array)




