def merge_sort(arr):
  """Sorts a list using the merge sort algorithm.

  Args:
    arr: The list to be sorted.

  Returns:
    The sorted list.
  """

  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
  """Merges two sorted lists into a single sorted list.

  Args:
    left: The left sorted list.
    right: The right sorted list.

  Returns:
    The merged sorted list.
  """

  result = []
  left_index, right_index = 0, 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    else:
      result.append(right[right_index])
      right_index += 1

  # Append remaining elements from the left list if any
  result.extend(left[left_index:])

  # Append remaining elements from the right list if any
  result.extend(right[right_index:])

  return result

my_array = [1, 3, 6, 4, 2, 6, 7, 9, 24, 23, 53, 87]

new_array = merge_sort(my_array)

print(new_array)  # Output: [1, 2, 3, 4, 6, 6, 7, 9, 23, 24, 53, 87]
