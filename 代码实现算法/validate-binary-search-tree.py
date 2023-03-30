#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def demo(self, x: TreeNode) -> bool:
        values = lambda x: [] if not x else values(x.left) + [x.val] + values(x.right)
        a = values(root)
        return all([a[i] < a[i + 1] for i in range(len(a) - 1)])


if __name__ == "__main__":
    root = [2, 1, 3]
    result = Solution().demo(root)
    print(result)
