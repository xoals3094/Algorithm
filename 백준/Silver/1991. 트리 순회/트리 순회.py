import sys


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

N = int(sys.stdin.readline().strip())

tree = {chr(x): Node(chr(x), None, None) for x in range(ord('A'), ord('Z') + 1)}

for _ in range(N):
    P, C1, C2 = sys.stdin.readline().strip().split()
    parent = tree[P]
    if C1 != '.':
        parent.left = tree[C1]
    if C2 != '.':
        parent.right = tree[C2]

def preorder(node: Node):
    if node is None:
        return

    print(node.value, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node: Node):
    if node is None:
        return

    inorder(node.left)
    print(node.value, end='')
    inorder(node.right)

def postorder(node: Node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value, end='')


root = tree['A']
preorder(root)
print()
inorder(root)
print()
postorder(root)

