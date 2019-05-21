from binomial_tree import BinomialTree

class BinomialHeap:
  def __init__(self):
    self.trees = []
  
  def add_elem(self, key):
    tree = BinomialTree(initial_key=key)
    self.trees.append(tree)
    self._fix_heap()
  
  def union(self, heap):
    self.trees.extend(heap.trees)
    self._fix_heap()
  
  def get_min_tree(self):
    return min(self.trees, key = lambda tree: tree.root.key)
  
  def remove_min_node(self):
    min_tree = self.get_min_tree()
    self.trees.remove(min_tree)
    for root_child in min_tree.root.children:
      new_tree = BinomialTree(root=root_child)
      self.trees.append(new_tree)

    self._fix_heap() 
  
  def is_empty(self):
    return self.size() == 0
  
  def size(self):
    return len(self.trees)
  
  def clear(self):
    self.trees = []

  def _fix_heap(self):
    trees = self.trees
    trees.sort(key = lambda tree: tree.root.degree)
    was_merge = True

    while was_merge:
      was_merge = False
      for i in range(0, len(trees) - 1):
        if i >= len(self.trees) - 1:
          break
        
        if trees[i].root.degree == trees[i+1].root.degree:
          was_merge = True
          trees[i] = trees[i].union(trees[i+1])
          trees.pop(i+1)