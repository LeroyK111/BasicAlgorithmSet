#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
相同顺序类型的数据, 有顺序, 内存or硬盘中连续存放,间隔距离就是数据的bit
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)

# 占用bit
print(bin(a[0]), bin(a[1]))
# 存放内存位置
print(f"占用1bit:{hex(id(a[0]))}", f"占用2bit:{hex(id(a[1]))}")
