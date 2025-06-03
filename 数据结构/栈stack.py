#!/usr/bin/python
# -*- coding: utf-8 -*-

stack = []

# 入栈
stack.append(1)
stack.append(2)
stack.append(3)

# 出栈
print(stack.pop())  # 输出 3

# 查看栈顶元素
print(stack[-1])  # 输出 2

# 判空
print(len(stack) == 0)


# class实现
class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop() if not self.is_empty() else None

    def peek(self):
        return self.data[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


# 另一种实现
from collections import deque

stack = deque()

# 入栈
stack.append("a")
stack.append("b")

# 出栈
print(stack.pop())  # 输出 b

# 栈顶
print(stack[-1])  # 输出 a
