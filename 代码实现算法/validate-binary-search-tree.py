#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
from TreeNode import Node


class Solution:
    def __init__(self, iput):
        self.data = iput

    def demo(self, x: Node) -> bool:
        result = x.PreorderTraversal(x)
        print(result)
        if result == self.data:
            return True
        return False


if __name__ == "__main__":
    data = [2, 1, 3]
    # data = [5, 1, 4, None, None, 3, 6]
    # 这里是前序遍历的结果, 利用结果反向生成树，然后
    root = Node(data[0])
    for i in data[1:]:
        root.insert(i)
    result = Solution(data).demo(root)
    print(result)
