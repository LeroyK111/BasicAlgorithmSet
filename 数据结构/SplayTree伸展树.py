#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Splay Tree（伸展树） 是一种自调整的二叉搜索树（Self-adjusting BST），由 Sleator 和 Tarjan 于 1985 年提出。

它的特别之处是：

最近访问的节点会被提升到根节点（称为 Splay 操作）

让频繁访问的节点更接近根部，提高后续访问效率

不需要额外的平衡因子（不像 AVL 或红黑树），靠访问时的自我调整来“渐进式”保持平衡

"""


class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y


def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y


def splay(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        if not root.left:
            return root
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = left_rotate(root.left)
        return right_rotate(root) if root.left else root
    else:
        if not root.right:
            return root
        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = right_rotate(root.right)
        return left_rotate(root) if root.right else root


def insert_splay(root, key):
    if not root:
        return SplayNode(key)
    root = splay(root, key)
    if root.key == key:
        return root
    new_node = SplayNode(key)
    if key < root.key:
        new_node.right = root
        new_node.left = root.left
        root.left = None
    else:
        new_node.left = root
        new_node.right = root.right
        root.right = None
    return new_node


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


root = None
for key in [5, 3, 7, 2, 4]:
    root = insert_splay(root, key)

print("Splay 中序遍历:", inorder(root))
