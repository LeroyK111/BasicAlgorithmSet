#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1 2 3
4 5 6
7 8 9


顺时针旋转90度
7 4 1
8 5 2
9 6 3



直接计算，横排转竖排,然后返回
"""


def demo(matrix: list) -> list:
    # 直接计算竖排
    data = {}
    n = len(matrix[0])
    for i in range(n):
        if str(i) not in data.keys():
            data[str(i)] = []

        for y in range(n - 1, -1, -1):
            data[str(i)].append(matrix[y][i])

    return list(data.values())


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    result = demo(matrix)
    print(result)