#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

| 特性       | B-Tree      | B+ Tree        |
| -------- | ----------- | -------------- |
| 所有键值存储位置 | 内部节点和叶子节点都有 | 只在叶子节点         |
| 是否适合范围查询 | 较难          | **非常高效**（叶子链表） |
| 数据访问跳跃性  | 随机          | 更连续，利于顺序读      |

"""


class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)

        # z 拿右半部分 keys
        z.keys = y.keys[t:]  # 右边 t-1 个
        mid_key = y.keys[t - 1]  # 中间 key
        y.keys = y.keys[: t - 1]  # 左边 t-1 个

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, mid_key)

    def print_tree(self, level=0):
        print("  " * level + f"Level {level} Keys: {self.keys}")
        for child in self.children:
            child.print_tree(level + 1)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, key):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
        self.root.insert_non_full(key)

    def print_tree(self):
        self.root.print_tree()


# 测试插入
btree = BTree(t=2)
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(key)

btree.print_tree()
