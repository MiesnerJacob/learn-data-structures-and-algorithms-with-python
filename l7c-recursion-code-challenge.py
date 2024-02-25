# Function that takes list and value and moves value to end of list
def move_to_end(lst, val):
    if lst == [] or len(lst) == 1:
        return lst
    if lst[0] == val:
        return move_to_end(lst[1:], val) + [lst[0]]
    else:
        return [lst[0]] + move_to_end(lst[1:], val)


# Test move to end
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))


class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def flatten(self):
        temp = self
        result = []
        while temp:
            result.append(temp.value)
            temp = temp.next_node
        return result

class LinkedList:
    def __init__(self):
        self.head = None
    def __init__(self, lst):
        self.head = ListNode(lst[0])
        current = self.head
        for val in lst[1:]:
            current.next_node = ListNode(val)
            current = current.next_node
    def append(self, value):
        temp = ListNode(value)
        if self.head is None:
            self.head = temp
            return
        
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = temp

def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    return head


# Test remove node functions
gemstones = LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())


def wrap_string(str, n):
  result = ""
  if n <= 0:
    return str
  result += "<"
  result += wrap_string(str, n-1)
  result += ">"

  return result
  
# Test wrap string function
wrapped = wrap_string("Pearl", 3)
print(wrapped)