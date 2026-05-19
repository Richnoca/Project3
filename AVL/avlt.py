from avl import Node, _insert, _balance_factor, _height, _rebalance
import random


def inorder(root):
    values = []

    def walk(node):
        if node:
            walk(node.left)
            values.append(node.key)
            walk(node.right)

    walk(root)
    return values

def display_levels(root):

    if root is None:
        print("(empty tree)")
        return

    queue = [(root, 0)]
    current_level = 0
    line = "Level 0: "

    while queue:
        node, level = queue.pop(0)

        if level != current_level:
            print(line)
            current_level = level
            line = f"Level {level}: "

        line += f"{node.key} "

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    print(line)

def check_avl(node): # checks nodes follow balance rule
    if node is None:
        return True

    balance = _balance_factor(node)

    if balance < -1 or balance > 1:
        print(f"AVL violation at node {node.key}")
        return False

    return check_avl(node.left) and check_avl(node.right)

def check_sorted(root): # chbecks keys are in sorted order
    values = inorder(root)
    return values == sorted(values)

def verify_tree(root, action): #verifies ordering and balance
    if not check_sorted(root):
        print(f"BST property failed after {action}")
        return False

    if not check_avl(root):
        print(f"AVL balance property failed after {action}")
        return False

    return True

def min_value_node(node): #finds smallest node in tree
    current = node

    while current.left is not None:
        current = current.left

    return current

def delete_node(root, key): # deletes a node with the given key and rebalances the tree
    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else: # no children
        if root.left is None and root.right is None:
            return None

        elif root.left is None: # only right child
            return root.right

        elif root.right is None: # only left child
            return root.left

        else: # two children
            successor = min_value_node(root.right)
            root.key = successor.key
            root.right = delete_node(root.right, successor.key)

    return _rebalance(root)

def run_insert_test(name, keys):
    print("\n" + "=" * 60)
    print(f"INSERT TEST: {name}")
    print("=" * 60)

    root = None

    for key in keys:
        root = _insert(root, key)

        if not verify_tree(root, f"inserting {key}"):
            return None

        print(f"Inserted {key:>3} | inorder = {inorder(root)}")

    print("\nFinal tree by level:")
    display_levels(root)

    print(f"\n{name} insert test passed!")

    return root

def run_delete_test(root, keys_to_delete):
    print("\n" + "=" * 60)
    print("DELETE TEST")
    print("=" * 60)

    for key in keys_to_delete:
        root = delete_node(root, key)

        if not verify_tree(root, f"deleting {key}"):
            return None

        print(f"Deleted {key:>3} | inorder = {inorder(root)}")

    print("\nTree after deletes by level:")
    display_levels(root)

    print("\nDelete test passed!")

    return root


if __name__ == "__main__":
    # sequential insertion
    sequential_keys = list(range(1, 21))

    # reverse insertion
    reverse_keys = list(range(20, 0, -1))

    # random insertion
    random.seed(42)
    random_keys = list(range(1, 21))
    random.shuffle(random_keys)

    # insert tests
    run_insert_test("Sequential Order", sequential_keys)
    run_insert_test("Reverse Order", reverse_keys)
    random_tree = run_insert_test("Random Order", random_keys)

    # delete keys from the random tree
    keys_to_delete = random_keys[:5]

    run_delete_test(random_tree, keys_to_delete)

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)
