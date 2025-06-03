#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
就是列表的用法, 仅在func上做区分
"""


from collections import deque

q = deque()

# 入队
q.append("A")
q.append("B")
q.append("C")

# 出队（从左边）
print(q.popleft())  # 输出 A
print(q.popleft())  # 输出 B

# 当前队列
print(q)  # deque(['C'])


import queue

# 适合多线程
q = queue.Queue()

# 入队
q.put("A")
q.put("B")

# 出队（会阻塞）
print(q.get())  # 输出 A
print(q.get())  # 输出 B
