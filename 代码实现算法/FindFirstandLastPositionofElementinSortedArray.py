#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


def demo(data: list, target: str) -> list:
    result = []
    if data.count(target) < 2:
        return [-1, -1]

    # start = data.index(target)
    # print(start)
    # end = data.index(target, start + 1)
    # print(end)

    # 写个分割取数
    for index, value in enumerate(data):
        if value == target:
            result.append(index)

    return [min(result), max(result)]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = demo(nums, target)
    print(result)