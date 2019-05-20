import math

def insert(root, node, complete_levels, curr_level):
  if not root:
    return False

  if curr_level == complete_levels:
    if root.left == None:
      node.parent = root
      root.left = node
      return True

    if root.right == None:
      node.parent = root
      root.right = node
      return True
    
    return False
  
  if insert(root.left, node, complete_levels, curr_level + 1):
    return True
  
  return insert(root.right, node, complete_levels, curr_level+1)

def fix_heap(root, should_fix):
  if not root or (not root.left and not root.right):
    return

  prev_root_parent = root.parent
  if root.left and should_fix(root, root.left):
    root.left.substitute_with_parent()
    fix_heap(prev_root_parent, should_fix)

  elif root.right and should_fix(root, root.right):
    root.right.substitute_with_parent()
    fix_heap(prev_root_parent, should_fix)

  else:
    fix_heap(root.left, should_fix)
    fix_heap(root.right, should_fix)
