# Implement sum to one to simulate the call stack utilized in a recursive function
def sum_to_one_call_stack(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while call_stack != []:
    return_value = call_stack[-1]
    call_stack.pop()
    print(call_stack)
    result += return_value["n_value"]
  return result, call_stack

def sum_to_one_recursive(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return sum_to_one_recursive(n-1) + n

def factorial(n):
  if n < 2:
    return 1
  return factorial(n - 1) * n

def power_set(my_list):
    if len(my_list) == 0:
        return [[]]
    
    power_set_without_first = power_set(my_list[1:])
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    return with_first + power_set_without_first

def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      flat_list = flatten(item)
      result.extend(flat_list)
    else:
      result.append(item)
  return result

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
def build_bst(my_list):
  if my_list == []:
    return "No Child"
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))

  tree_node = {"data": middle_value}

  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx + 1:])

  return tree_node

print("Sum to one function with call stack visualized")
print(sum_to_one_call_stack(4))
print('\n')

print("Sum to one recursive function")
print(sum_to_one_recursive(7))
print('\n')

print("Factorial recursive function")
print(factorial(12))
print('\n')

print("Power set recursive function")
universities = ['MIT', 'UCLA', 'Stanford', 'NYU', 'SDSU']
print([i for i in power_set(universities)])
print('\n')

print("Flatten recursive function")
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
print('\n')

print("Fibonacci recursive function")
print(fibonacci(8))
print('\n')

print("Build binary tree recursive function")
sorted_list = [12, 13, 14, 15, 16]
print(build_bst(sorted_list))
print('\n')