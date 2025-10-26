#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
本质就是多层链表,
跳表是一种支持快速搜索、插入、删除的有序数据结构，它用多层链表模拟“平衡树”的效果。

Level 3:       ──> 10 ───────> 50
Level 2:   ──> 5 ──> 10 ───────> 50
Level 1:  1 ──> 5 ──> 10 ──> 20 ─> 50 ─> 60

| 应用领域        | 为什么适合跳表         |
| ----------- | --------------- |
| Redis（ZSet） | 排序集合操作（范围查询、排名） |
| 数据库索引结构     | 插入快、查找快         |
| 内存排序容器      | 替代平衡树，结构简单，性能好  |
"""


import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # 多层指针


class SkipList:
    MAX_LEVEL = 4
    P = 0.5  # 每一层出现的概率

    def __init__(self):
        self.header = Node(None, self.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        # 从高层往低层查找插入位置
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current is None or current.value != value:
            lvl = self.random_level()
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = Node(value, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current and current.value == value


# 示例
s = SkipList()
for v in [10, 20, 30, 50, 40]:
    s.insert(v)

print(s.search(30))  # True
print(s.search(25))  # False
