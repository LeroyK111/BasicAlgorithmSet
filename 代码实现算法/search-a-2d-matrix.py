#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
编写一个高效的算法来判断 m x n矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
"""


class Solution(object):
    def __init__(self, matrix: list, target: int) -> None:
        self.matrix = matrix
        self.target = target
        self.res = False

    def count(self, data) -> bool:
        if self.target in data:
            return True

    def run(self) -> bool:
        # 不使用循环
        a = list(map(self.count, self.matrix))
        self.res = a[0]
        return self.res


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3

    res = Solution(matrix, target).run()
    print(res)
