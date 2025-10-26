#!/usr/bin/python
# -*- coding: utf-8 -*-

from bintrees import RBTree

"""
相比 AVL 树，红黑树稍微“不那么平衡”，但插入删除效率更高，适合高频动态更新场景。

Java：TreeMap / TreeSet 就是红黑树实现的
C++：std::map, std::set
Linux：完全基于红黑树的调度算法、内存映射表

读写,插入,删除 比 普通avl更快.
"""

tree = RBTree()
tree.insert(5, "a")
tree.insert(3, "b")
tree.insert(7, "c")

print("中序遍历:", list(tree.items()))
print("查找 3:", tree[3])
