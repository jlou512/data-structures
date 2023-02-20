
class Node:
  left = None
  right = None
  key = None
  value = None
  N = 0

  def __init__(self, key, value, size):
    self.key = key
    self.value = value
    self.N = size

class BinarySearchTree:
  root = None

  def get(self, key):    
    return self.__get(self.root, key)

  def __get(self, node, key):
    if node is None: return None    
    if key < node.key: return self.__get(node.left, key)
    elif key > node.key: return self.__get(node.right, key)
    else: return node

  def put(self, key, value):
    self.root = self.__put(self.root, key, value)

  def __put(self, node, key, value):      
    if node is None: return Node(key, value, 1)

    if key < node.key: node.left = self.__put(node.left, key, value)        
    elif key > node.key: node.right = self.__put(node.right, key, value)        
    else: node.value = value

    node.N = self.__size(node.left) + self.__size(node.right) + 1
    
    return node

  def delete(self, key):
    self.root = self.__delete(self.root, key)

  def __delete(self, node, key):
    if node is None:  return None
    if key < node.key: node.left = self.__delete(node.left, key)
    elif key > node.key: node.right =  self.__delete(node.right, key)
    else: 
      if node.right is None: return node.left
      if node.left is None: return node.right
      t = node
      node = self.__min(t.right)
      node.right = self.__delete_min(t.right)
      node.left = t.left
    return node

  def delete_min(self):
    self.root = self.__delete_min(self.root)
    
  def __delete_min(self, node):
    if node.left is None: return node.right
    node.left = self.__delete_min(node.left)
    node.N = self.__size(node.left) + self.__size(node.right) + 1
    return node
  
  def delete_max(self):
    self.root = self.__delete_max(self.root)

  def __delete_max(self, node):
    if node.right is None: return node.left
    node.right = self.__delete_max(node.right)
    node.N = self.__size(node.left) + self.__size(node.right) + 1
    return node

  def max(self):
    return self.__max(self.root)
  
  def __max(self, node):
    if node.right is None: return node
    return self.__max(node.right)
      
  def min(self):
    return self.__min(self.root)

  def __min(self, node):    
    if node.left is None: return node
    return self.__min(node.left)

  def size(self):
    return self.__size(self.root)

  def __size(self, node):
    if node == None:
      return 0
    return node.N

  def print(self):
    self.__print(self.root)    
  
  def __print(self, node):
    if node != None:      
      self.__print(node.left)
      print(node.key, ":", node.value)
      self.__print(node.right)

  def print_bfs(self):
    self.__print_bfs(self.root)

  def __print_bfs(self, node):
    current_level = list()    
    current_level.append(node)

    while current_level:
      next_level = list()      
      for x in current_level:
        print(x.key, ":", x.value, end=" ")
        if x.left: next_level.append(x.left)
        if x.right: next_level.append(x.right)

      current_level = next_level if len(next_level) > 0 else None
      print()
                  

#Unit Tests
bst = BinarySearchTree()
bst.put(10, "A")
bst.put(2, "B")
bst.put(33, "C")
bst.put(4, "D")
bst.put(1, "E")

assert bst.size() is 5
bst.print_bfs()

bst.delete_min()
assert bst.size() is 4
bst.print()
print(bst.get(33).value)
print(bst.get(4).value)
print(bst.get(10).value)
print(bst.get(2).value)
assert bst.max().key is 33
assert bst.min().key is 2

#Test non existing key lookup:
assert bst.get(56) is None
assert bst.get(5) is None
assert bst.get(11) is None

bst.delete_max()
assert bst.size() is 3
bst.print()

bst.put(13, "DASFAF")
bst.put(52, "ASLJFASF")

print()
print()

bst.print_bfs()
print()
bst.delete(4)
bst.print_bfs()



