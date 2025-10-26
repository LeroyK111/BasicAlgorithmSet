#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
!二叉排序树（BST, Binary Search Tree）
定义：

一棵二叉树，满足以下性质：

每个节点的左子树所有节点值 < 当前节点值

每个节点的右子树所有节点值 > 当前节点值

没有对高度或结构进行任何限制

问题：如果插入数据是有序的，就会退化成链表，查找效率 O(n)

!平衡二叉搜索树（Balanced BST）
定义：

是一种改进的 BST

在满足 BST 性质的基础上，保持树的高度平衡

常见的实现包括：

AVL 树

红黑树（Red-Black Tree）

Splay Tree（伸展树）

Treap

Scapegoat Tree

它们的目标是让查找、插入、删除的时间复杂度维持在 O(log n)，防止退化为链表。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = sorted_array_to_bst(nums[:mid])
    node.right = sorted_array_to_bst(nums[mid + 1 :])
    return node


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


# 示例
nums = [10, 20, 25, 30, 35, 40, 50]
root = sorted_array_to_bst(nums)

result = level_order(root)
print(result)
