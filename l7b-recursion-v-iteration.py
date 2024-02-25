def factorial_recursive(n):
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial_recursive(n - 1)


def factorial_iterative(n):
  if n == 0:
      return 1
  result = 1
  for i in range(1, n + 1):
      result *= i
  return result


def fibonacci_recursive(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    first = 0
    second = 1
    for _ in range(2, n + 1):
        new = first + second
        first = second
        second = new
    return new


def sum_digits_recursive(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits_recursive(n//10) + last_digit


def sum_digits_iterative(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n != 0:
    result += n % 10
    n = n // 10
  return result + n


def find_min_recursive(my_list):
  if my_list == []:
    return None
  if len(my_list) == 1:
      return my_list[0]
  else:
      return min(my_list[0], find_min_recursive(my_list[1:]))

def find_min_iterative(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min


def is_palindrome_recursive(my_string):
    if len(my_string) <= 1:
        return True
    if my_string[0] != my_string[-1]:
        return False
    return is_palindrome_recursive(my_string[1:-1])


def is_palindrome_iterative(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 


def multiplication_recursive(num_1, num_2):
  if num_1 == 0 or num_2 == 0:
    return 0
  return num_1 + multiplication_recursive(num_1, num_2 - 1)


def multiplication_iterative(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

def depth_recursive(tree):
    if not tree:
        return 0
    left_depth = depth_recursive(tree.get("left_child", None))
    right_depth = depth_recursive(tree.get("right_child", None))
    return max(left_depth, right_depth) + 1

def depth_iterative(tree):
    result = 0
    queue = [tree]
    while queue:
        level_count = len(queue)
        for child_count in range(0, level_count):
            child = queue.pop(0)
            if child.get("left_child"):
                queue.append(child["left_child"])
            if child.get("right_child"):
                queue.append(child["right_child"])
        result += 1
    return result

# Test factorial functions
print(factorial_recursive(3) == 6)
print(factorial_iterative(3) == 6)

# Test fibonacci functions
print(fibonacci_recursive(7) == 13)
print(fibonacci_iterative(7) == 13)

# Test sum digits functions
print(sum_digits_recursive(552) == 12)
print(sum_digits_iterative(552) == 12)

# Test find min functions
print(find_min_recursive([42, 17, 2, -1, 67]) == -1)
print(find_min_iterative([42, 17, 2, -1, 67]) == -1)

# Test is palindrome functions
print(is_palindrome_recursive("racecar") == True)
print(is_palindrome_iterative("racecar") == True)

# Test multiplication functions
print(multiplication_recursive(3, 7) == 21)
print(multiplication_iterative(3, 7) == 21)

# Test binary tree depth functions
four_level_tree = {
"data": 54,
"right_child":
  {"data": 93,
   "left_child":
     {"data": 63,
      "left_child":
        {"data": 59}
      }
   }
}
print(depth_recursive(four_level_tree) == 4)
print(depth_iterative(four_level_tree) == 4)