#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # 子节点列表

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"


def dfs(node, depth=0):
    """
    深度优先搜索遍历树结构，并打印节点值。
    """
    print("  " * depth + str(node.value))
    for child in node.children:
        dfs(child, depth + 1)


if __name__ == "__main__":
    # 创建根节点
    root = TreeNode("A")
    print("根节点:", root)

    # 创建四个子节点
    node_b = TreeNode("B")
    node_c = TreeNode("C")
    node_d = TreeNode("D")
    node_e = TreeNode("E")

    # 构建树结构
    root.add_child(node_b)
    root.add_child(node_c)
    root.add_child(node_d)
    node_c.add_child(node_e)

    dfs(root)
