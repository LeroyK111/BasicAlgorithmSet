#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


"""
     1
 2       3
4 5  none noe
"""


# 构造示例树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 打印遍历结果
print("前序遍历（根 → 左 → 右）:", preorder(root))  # [1, 2, 4, 5, 3]
print("中序遍历（左 → 根 → 右）:", inorder(root))  # [4, 2, 5, 1, 3]
print("后序遍历（左 → 右 → 根）:", postorder(root))  # [4, 5, 2, 3, 1]
