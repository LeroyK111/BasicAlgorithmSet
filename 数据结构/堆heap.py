#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
堆（heap）本质上就是一种用数组表示的完全二叉树结构
"""


import heapq

# 创建一个空堆（使用列表）
min_heap = []

# 插入元素
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 10)

print("当前堆（数组形式）:", min_heap)

# 访问最小值（堆顶）
print("堆顶元素（最小值）:", min_heap[0])

# 弹出最小值
min_val = heapq.heappop(min_heap)
print("弹出堆顶:", min_val)
print("更新后的堆:", min_heap)


# 原始数据
nums = [5, 1, 8, 3, 10]
# 建立最大堆（取负）
max_heap = []
for num in nums:
    heapq.heappush(max_heap, -num)  # 取负数模拟最大堆

print("当前最大堆（内部存的是负数）:", max_heap)

# 查看堆顶元素（最大值）
print("堆顶最大值:", -max_heap[0])

# 弹出堆顶元素
max_val = -heapq.heappop(max_heap)
print("弹出最大值:", max_val)
print("更新后的堆:", [-x for x in max_heap])
