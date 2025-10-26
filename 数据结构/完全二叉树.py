#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class CompleteBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # 创建节点
        new_node = TreeNode(val)
        if not self.root:
            # 如果树为空，则新节点为根节点
            self.root = new_node
            return

        # 使用队列进行层序遍历插入
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                # 如果左子节点为空，则将新节点插入左子节点
                node.left = new_node
                return
            elif not node.right:
                # 如果右子节点为空，则将新节点插入右子节点
                node.right = new_node
                return
            else:
                # 如果左右子节点都存在，则继续遍历
                queue.append(node.left)
                queue.append(node.right)

    def level_order(self):
        result = []
        if not self.root:
            return result

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


# 示例用法
tree = CompleteBinaryTree()
for i in [2, 5, 1, 0, 7, 9, 8, 10, 3, 4, 6]:
    tree.insert(i)

# 最小堆
print("层序遍历结果:", tree.level_order())
