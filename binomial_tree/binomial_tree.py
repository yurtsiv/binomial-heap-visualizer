import math
import uuid
from .node import Node

class BinomialTree:
  def __init__(self, root=None, initial_key=None):
    self.id = uuid.uuid4()

    if root:
      self.root = root
    elif initial_key:
      self.root = Node(initial_key, 0)

  def union(self, tree):
    if tree.root.degree != self.root.degree:
      raise Exception("Can't union trees with different degrees")

    if self.root.key <= tree.root.key:
      self.root.childs.append(tree.root)
      self.root.degree += 1
      return self

    tree.root.degree += 1
    tree.root.childs.append(self.root)
    return tree
  
  def is_empty(self):
    return self.root == None

  def clear(self):
    self.root = None
  
  def size(self):
    return pow(self.root.degree, 2)
