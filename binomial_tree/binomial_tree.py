import math
from .node import Node
from .draw import draw_tree

class BinomialTree:
  def __init__(self, initial_key):
    self.root = Node(initial_key, 0)
    self.degree = 0

  def union(self, tree):
    if tree.degree != self.degree:
      raise Exception("Can't union trees with different degrees")

    if self.root.key <= tree.root.key:
      self.root.childs.append(tree.root)
      self.degree += 1
      return self

    tree.degree += 1
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
