#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_full_binary_tree(depth, start_val=1):
    if depth == 0:
        return None

    # 创建当前节点
    root = TreeNode(start_val)
    # 递归构建左子树
    root.left = build_full_binary_tree(depth - 1, start_val * 2)
    # 递归构建右子树
    root.right = build_full_binary_tree(depth - 1, start_val * 2 + 1)
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


# 构造深度为 3 的满二叉树
tree_root = build_full_binary_tree(3)
print("层序遍历:", level_order(tree_root))
