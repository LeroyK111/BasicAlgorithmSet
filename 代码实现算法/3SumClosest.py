#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list, target: int) -> list:
    result = []
    newdata = list(map(lambda x: abs(target - x), data))
    for i in range(3):
        minIndex = newdata.index(min(newdata))
        newdata.pop(minIndex)
        result.append(data[minIndex])

    return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 0

    result = demo(nums, target)
    print(result)