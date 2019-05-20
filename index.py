import tkinter as tk
from binomial_heap import BinomialHeap

heap = BinomialHeap()
heap.add_elem(1)
heap.add_elem(2)
heap.add_elem(3)
heap.add_elem(4)
heap.add_elem(5)
heap.add_elem(6)

heap_2 = BinomialHeap()
heap_2.add_elem(1)
heap_2.add_elem(2)
heap_2.add_elem(3)
heap_2.add_elem(4)
heap_2.add_elem(5)
heap_2.add_elem(6)

heap.union(heap_2)
print("")
# root = tk.Tk()
# root.title('Heap')
# App(root)
# root.mainloop()