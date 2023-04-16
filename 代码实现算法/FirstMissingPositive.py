#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
找最小的缺失正整数
"""


def demo(nums: list) -> int:
    # 过滤负数
    data = list(filter(lambda x: x > 0, nums))
    for i in range(1, max(data) + 1):
        if i in data:
            continue
        elif i == max(data):
            return max(data) + 1
        else:
            return i


if __name__ == '__main__':
    data = [3, 4, 1, -1, 0]
    result = demo(data)
    print(result)
