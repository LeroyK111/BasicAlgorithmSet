#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
"""
无重复数组
"""


def demo(data: list) -> list:
    result = []
    maxValue = 1
    indexmax = len(data)
    # 计算全排列数量
    for i in range(len(data), 1, -1):
        maxValue = maxValue * i

    # 随机数取值
    while True:
        c = data.copy()
        a = []
        for i in range(indexmax):
            b = random.choice(c)
            c.remove(b)
            a.append(b)

        if a in result:
            continue

        result.append(a)

        if len(result) == maxValue:
            return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    result = demo(nums)
    print(result)