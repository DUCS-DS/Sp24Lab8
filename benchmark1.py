from random import randint
from time import time
from balancedbst import BST, BBST
from redblacktree import RedBlackTree
from avltree import AVLTree

def build_time(n, tree):
   start = time()
   for _ in range(n):
       tree.insert(randint(1, 1000))
   if isinstance(tree, BBST):
       tree.balance()
   return time() - start

n = 2**15
print(f"time to insert n={n} items:")
print("BST", build_time(n, BST()))
print("BBST", build_time(n, BBST()))
print("RBT", build_time(n, RedBlackTree()))
print("AVL", build_time(n, AVLTree()))

n = 10 * n
print("\ntime to insert 10*n items:")
print("BST", build_time(n, BST()))
print("BBST", build_time(n, BBST()))
print("RBT", build_time(n, RedBlackTree()))
print("AVL", build_time(n, AVLTree()))
