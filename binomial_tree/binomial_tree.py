import math
from .node import Node
from .draw import draw_tree

class BinomialTree:
  def __init__(self, root=None, initial_key=None):
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
  
  def draw(self, canvas, init_pos):
    draw_tree(
      self.root,
      None,
      init_pos,
      1,
      { 'canvas': canvas }
    )

  def is_empty(self):
    return self.root == None

  def clear(self):
    self.root = None
  
  def size(self):
    return pow(self.root.degree, 2)
