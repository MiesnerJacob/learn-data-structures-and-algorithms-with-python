# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Test Node Implementation
my_node = Node(value=44)
print(my_node.get_value())

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(value=new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    list_str = ''
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        list_str += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
    return list_str  
  
  def remove_first_node_with_value_match(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
  
  def swap_nodes(self, input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
        print("Elements are the same - no swap needed")
        return

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

def nth_last_node(linked_list, n):
  nth_last_pointer = None
  tail_pointer = linked_list.head_node
  count = 1

  while tail_pointer:
    tail_pointer = tail_pointer.get_next_node()
    count += 1

    if count >= n + 1:
      if nth_last_pointer is None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()

  return nth_last_pointer

# Test LinkedList Implementation
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())