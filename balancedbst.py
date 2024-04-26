class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self, level=0):
        string = "   " * level + str(self.data) + "\n"
        for child in [self.left, self.right]:
            if child:
                string += child.__str__(level + 1)
        return string


class Tree:
    """Binary tree."""

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def traversal(self):
        """Return the in-order (morris) traversal as a list.

        Note: the time-complexity here is O(n) where n is the
              number of nodes.
        """
        lst = []
        node = self.root
        while node:
            if not node.left:
                lst.append(node.data)
                node = node.right
            else:
                precursor = node.left
                while precursor.right and precursor.right != node:
                    precursor = precursor.right
                if not precursor.right:
                    precursor.right = node
                    node = node.left
                else:
                    precursor.right = None
                    lst.append(node.data)
                    node = node.right
        return lst

    def height(self):
        """Return the height of the tree."""
        return _height(self.root) if self.root else None


def _height(node):
    """Helper for height method."""

    if not node:
        return -1
    leftheight = _height(node.left)
    rightheight = _height(node.right)
    return max(leftheight, rightheight) + 1


class BST(Tree):
    """Binary Search Tree"""

    def __init__(self):
        super().__init__()

    def insert(self, item):
        if not self.root:
            self.root = Node(item)
        else:
            node = self.root
            while node:
                if item < node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(item)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(item)
                        break

    def search(self, item):
        node = self.root
        while node:
            if item == node.data:
                return node.data
            elif item < node.data:
                node = node.left
            else:
                node = node.right


class BBST(BST):
    """Balancable Binary Search Tree"""

    def __init__(self):
        super().__init__()

    def balance(self):
        self.root = _balance(self.traversal())


def _balance(lst):

    #
    #  YOUR CODE GOES HERE
    #


if __name__ == "__main__":

    from random import randint

    bbst = BBST()
    bst = BST()
    n = 18
    for _ in range(n):
        item = randint(1, 7)
        bbst.insert(item)
        bst.insert(item)
    bbst.balance()
    print(bst)
    print("unbalanced height:", bst.height())
    print()
    print(bbst)
    print("balanced height:", bbst.height())
