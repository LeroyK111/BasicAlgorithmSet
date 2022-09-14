#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Input: nums = [1,3,5,6], target = 2
Output: 1
"""


def demo(data: list, target: list) -> int:
    try:
        result = data.index(target)
    except ValueError:
        if min(data) > target:
            return 0
        elif max(data) < target:
            return len(data)

        for index, value in enumerate(data):
            if target > value and target < data[index + 1]:
                return index + 1
    else:
        return result


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    nums.sort()
    target = 2
    result = demo(nums, target)
    print(result)
