def binary_search_recursion(sorted_list, left_pointer, right_pointer, target):
  if left_pointer >= right_pointer:
    return "value not found"
	
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    return binary_search_recursion(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    return binary_search_recursion(sorted_list, mid_idx + 1, right_pointer, target)
  
def binary_search_iterative(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  while left_pointer < right_pointer:
    mid_idx = (right_pointer + left_pointer) // 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      right_pointer = mid_idx
    if target > mid_val:
      left_pointer = mid_idx + 1

  return "Value not in list"


# Test binary search recursive function
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search_recursion(values, start_of_values, end_of_values, 300)
print("element {0} is located at index {1}".format(300, result))

# Test binary search iterative function
values = [77, 80, 102, 123, 288, 300, 540]
result = binary_search_iterative(values, 300)
print("element {0} is located at index {1}".format(300, result))