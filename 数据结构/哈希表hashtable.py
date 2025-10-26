#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
其实就是字典dict

使用数组来处理冲突,主要是hash(key)的问题.
"""


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 用链表数组处理冲突（拉链法）

    def _hash(self, key):
        # 简单哈希函数：将 key 转为整数并取模
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        # 检查是否已存在此 key，更新值
        # print(index)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # 否则添加新键值对
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # 没找到

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


ht = HashTable()

ht.set("apple", 3)
ht.set("abcde", 3)
ht.set("banana", 5)
ht.set("grape", 10)

print("get('apple'):", ht.get("apple"))
print("get('banana'):", ht.get("banana"))

ht.set("apple", 99)  # 更新
print("更新后的 get('apple'):", ht.get("apple"))

ht.remove("banana")
print("删除后 get('banana'):", ht.get("banana"))

ht.display()
