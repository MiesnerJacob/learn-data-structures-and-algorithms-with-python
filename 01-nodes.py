# Define Node class
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Create a few nodes
yacko = Node(value="likes to yak")
wacko = Node(value="has a penchant for hoarding snacks")
dot = Node(value="enjoys spending time in movie lots")

# Link some of the nodes
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# get values of nodes linked to nodes
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

# print values returned above
print(dots_data)
print(wackos_data)