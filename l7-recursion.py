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

print(factorial(12))

print("Sum to one function with call stack visualized")
print(sum_to_one_call_stack(4))
print('\n')

print("Sum to one recursive function")
print(sum_to_one_recursive(7))
print('\n')

print("Factorial recursive function")
print(factorial(12))
print('\n')