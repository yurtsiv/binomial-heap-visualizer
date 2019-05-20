from binomial_tree import BinomialTree

class BinomialHeap:
  def __init__(self):
    self.trees = []
  
  def add_elem(self, key):
    tree = BinomialTree(key)
    self.trees.append(tree)
    self._fix_heap()
  
  def union(self, heap):
    self.trees.extend(heap.trees)
    self.trees.sort(key = lambda x: x.degree)
    self._fix_heap()
  
  def _fix_heap(self):
    trees = self.trees
    merged = True

    while merged:
      merged = False
      for i in range(0, len(trees) - 1):
        if i >= len(self.trees):
          break
        
        if trees[i].degree == trees[i+1].degree:
          merged = True
          trees[i] = trees[i].union(trees[i+1])
          trees.pop(i+1)