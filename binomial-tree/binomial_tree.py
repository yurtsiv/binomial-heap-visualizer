import uuid
import math
from .node import Node
from .draw import draw_tree
from .utils import *

class BinomialTree:
  def __init__(self):
    self._root = self.min = self.max = None
    self.size = self.complete_levels = 0
    self.keys = []

  def _handle_size_increase(self):
    self.size += 1
    self.complete_levels = math.floor(math.log2(self.size + 1))

  def _create_node(self, key):
    return Node(uuid.uuid4(), key)
  
  def _insert(self, node):
    if not self._root:
      self._root = node 
    else:
      insert(self._root, node, self.complete_levels, 1)

  def _should_fix(self, parent, child):
    return child.key < parent.key

  def add(self, key):
    self.keys.append(key)
    node = self._create_node(key)
    self._insert(node)

    self._handle_size_increase()
    fix_heap(self._root, self._should_fix)

    if not self.max and not self.min:
      self.max = self.min = key
    elif key > self.max:
      self.max = key
    elif key < self.min:
      self.min = key

    # if the node became a new root
    if self._should_fix(self._root, node):
      self._root = node

  def draw(self, canvas, init_pos):
    draw_tree(
      self._root,
      None,
      init_pos,
      1,
      { 'canvas': canvas, 'tree_size': self.size, 'tree_depth': self.complete_levels + 1 }
    )
