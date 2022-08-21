#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def count(dt):
    # 形参得到的是实参的内存位置，并不是copy创建了新变量
    print(id(dt))

    oneIndex = random.randint(0, len(dt) - 1)
    one = dt[oneIndex]
    dt.remove(one)
    twoIndex = random.randint(0, len(dt) - 1)
    two = dt[twoIndex]
    dt.remove(two)
    threeIndex = random.randint(0, len(dt) - 1)
    three = dt[threeIndex]

    if sum([one, two, three]) == 0:
        return [one, two, three]
    else:
        return None


def demo():
    # !又或者不断赋值，保护原始变量
    data = [1, -1, 0, -2, 3]

    while True:
        a = data
        print(id(a))
        result = count(a)
        if result is not None:
            return result


if __name__ == '__main__':
    result = demo()
    print(result)
