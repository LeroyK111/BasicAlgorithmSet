#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

"""
Treap = Tree + Heap

Treap 是一种二叉搜索树，它在每个节点上引入一个“优先级（priority）”字段，使整棵树既满足 BST 的性质，又满足堆的性质。

它在结构上是 BST（二叉搜索树）

它在逻辑上遵循堆（最小堆或最大堆）

这种设计带来的是一个概率平衡的结构，插入和删除的平均时间复杂度为 O(log n)，最坏为 O(n)，但几率极小。

时间复杂度与 AVL/红黑树相似，但实现更简单
随机优先级使其在实际应用中“几乎总是平衡”
插入删除逻辑更清晰，特别适合手写或教学
"""


class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 100)
        self.left = None
        self.right = None


def rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    return q


def rotate_left(p):
    q = p.right
    p.right = q.left
    q.left = p
    return q


def treap_insert(root, key):
    if not root:
        return TreapNode(key)
    if key < root.key:
        root.left = treap_insert(root.left, key)
        if root.left.priority < root.priority:
            root = rotate_right(root)
    else:
        root.right = treap_insert(root.right, key)
        if root.right.priority < root.priority:
            root = rotate_left(root)
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


root = None
for key in [5, 3, 7, 2, 4]:
    root = treap_insert(root, key)

print("Treap 中序遍历:", inorder(root))
