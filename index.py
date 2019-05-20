import tkinter as tk
from binomial_tree import BinomialTree
# from gui import App

a = BinomialTree(1)
b = BinomialTree(2)
ab = a.union(b)

c = BinomialTree(3)
d = BinomialTree(6)
cd = c.union(d)

abcd = ab.union(cd)

print("")
# root = tk.Tk()
# root.title('Heap')
# App(root)
# root.mainloop()