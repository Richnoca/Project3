class Node:
    def __init__(self, key):
        self.key    = key
        self.left   = None # left pointer
        self.right  = None # right pointer
        self.height = 1 #height of node starts at 1 for leaf nodes


# returns height of node, if no node then height is 0
def _height(node):
    return node.height if node else 0

#returns balance factor, bf = height(left subtree) - height(right subtree)
def _balance_factor(node):
    return _height(node.left) - _height(node.right)

#updates based on height of children
def _update_height(node):
    node.height = 1 + max(_height(node.left), _height(node.right))

#left side too heavy, rotate right
def _rotate_right(y):
    x, B = y.left, y.left.right

    x.right = y
    y.left  = B

    _update_height(y)
    _update_height(x)

    return x # new root after rotation

#right side too heavy, rotate left
def _rotate_left(x):
    y, B = x.right, x.right.left

    y.left  = x
    x.right = B

    _update_height(x)
    _update_height(y)

    return y # new root after rotation


# Rebalance the node if necessary and return the new root of the subtree
def _rebalance(node):
    _update_height(node) #update height first to get correct balance factor
    bf = _balance_factor(node) # whats the balance factor

    if bf > 1: # left side is too heavy here
        if _balance_factor(node.left) < 0:  # Left-Right
            node.left = _rotate_left(node.left) # left child is right heavy so rotate left first

        return _rotate_right(node) # Left-Left

    if bf < -1: # Right side is too heavy here
        if _balance_factor(node.right) > 0: # Right-Left
            node.right = _rotate_right(node.right) # right child is left heavy so rotate right first

        return _rotate_left(node) # Right-Right

    return node # already balanced then just return unchanged

def _insert(node, key):
    if node is None:
        return Node(key) # insert new node here

    if key < node.key: # key is smaller than current node, go left
        node.left  = _insert(node.left,  key)
    elif key > node.key: # key is larger than current node, go right
        node.right = _insert(node.right, key)
    else: 
        return node  # key exists dont insert duplicate

    return _rebalance(node) # after inserting, rebalance the tree and return new root of subtree

class AVLTree:
    def __init__(self):
        self.root = None # empty tree / no root

    def insert(self, key):
        self.root = _insert(self.root, key) # insert key and update root in case it changes due to rotations

    def inorder(self): # return keys in order
        result = []
        def _walk(node):
            if node:
                _walk(node.left) # visit left subtree first
                result.append(node.key)
                _walk(node.right) # visit right subtree last
        _walk(self.root) # recursive walk starting from root
        return result

    def height(self):
        return _height(self.root)
