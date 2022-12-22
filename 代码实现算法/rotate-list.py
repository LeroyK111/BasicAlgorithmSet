#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list, k: int = 0) -> list:
    """
    直接位置循环
    """
    res = [*data]
    n = len(data)
    for i, v in enumerate(data):
        index = k % n + i
        if index >= n:
            index = index % n
        res[index] = v

    return res


if __name__ == "__main__":
    data = [1, 2, 3]
    k = 5
    res = demo(data, k)
    print(res)
