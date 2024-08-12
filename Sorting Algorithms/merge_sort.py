

def merge_sort(arr):
    
    #Base case: if the list has one of fewer elements, its already sorted
    if  len(arr)  <= 1:
        return arr
    #find the middle index of the list
    mid = len(arr)//2
    
    #divide the list into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    #recursively sort the left and  right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)


#merge the sorted halves into a single sorted list
    return merge(left_half, right_half)    

def merge (left, right):
    #merges the sorted lists into a single sorted list.
    
    #create an empty list to store the merged result
    result = []
    
    #initialize indices for left and right lists
    left_index, right_index = 0, 0
    
    #compare elements from both lists and append the smaller one to the result 
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
            
    #Append remaining elements from the left list if any
    result.append(left[left_index])
    
    #Append remaining elements from the right list if any
    result.extend(right[right_index])
    
    return result



my_array = [1,3,6,4,2,6,7,9,24,23,53,87]

new_array = merge_sort(my_array)

print(new_array)
    
# output: [1, 2, 3, 4, 6, 6, 7, 9, 23, 24, 53, 87]
