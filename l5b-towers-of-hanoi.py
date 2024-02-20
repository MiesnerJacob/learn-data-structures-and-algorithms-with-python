class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
      pointer = self.top_item
      print_list = []
      while(pointer):
          print_list.append(pointer.get_value())
          pointer = pointer.get_next_node()
      print()
      
      print(f"Stack {self.name}: ", end="")
      visual_representation = ""
      print(print_list)
      for value in reversed(print_list):
          visual_representation = ' ' * (self.limit - value) + '█' * (value * 2) + "\n" + visual_representation

      print(visual_representation.rstrip(), end="")


def setup_game():
    print("\nLet's play Towers of Hanoi!!")
    stacks = [Stack(name="Left"), Stack(name="Middle"), Stack(name="Right")]

    num_disks = int(input("\nHow many disks do you want to play with?\n"))
    while num_disks < 3:
        num_disks = int(input("Enter a number greater than or equal to 3\n"))

    for disk in range(num_disks, 0, -1):
        stacks[0].push(disk)

    print(f"\nThe fastest you can solve this game is in {2 ** num_disks - 1} moves")
    return stacks, num_disks

def get_input(stacks):
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i, stack in enumerate(stacks):
            print(f"Enter {choices[i]} for {stack.get_name()}")
        user_input = input("").upper()
        if user_input in choices:
            return stacks[choices.index(user_input)]

def play_game(stacks, num_disks):
    num_user_moves = 0
    while stacks[-1].get_size() != num_disks:
        print("\n\n\n...Current Stacks...")
        for stack in stacks:
            stack.print_items()
        from_stack = get_move("move from", stacks)
        to_stack = get_move("move to", stacks)
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif not to_stack.is_empty() and from_stack.peek() > to_stack.peek():
            print("\n\nInvalid Move. Try Again")
        else:
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1

    print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {2 ** num_disks - 1}")

def get_move(action, stacks):
    while True:
        print(f"\nWhich stack do you want to {action}?\n")
        stack = get_input(stacks)
        if action == "move from" and stack.is_empty():
            print("\nInvalid Move. Try Again")
        else:
            return stack

if __name__ == "__main__":
    stacks, num_disks = setup_game()
    play_game(stacks, num_disks)
