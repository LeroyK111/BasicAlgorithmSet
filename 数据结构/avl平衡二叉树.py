#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
一般说平衡二叉树: 特指 AVL 树

以下则是变种:
红黑树
Treap / Splay 树
平衡 BST
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sorted_array_to_balanced_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_balanced_bst(arr[:mid])
    root.right = sorted_array_to_balanced_bst(arr[mid + 1 :])
    return root


def level_order(root):
    from collections import deque

    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# 构建平衡二叉树（输入需为有序数组）
arr = range(8)  # 示例有序数组
tree_root = sorted_array_to_balanced_bst(arr)
print("层序遍历:", level_order(tree_root))
