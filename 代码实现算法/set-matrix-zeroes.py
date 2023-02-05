#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self, data: list) -> None:
        self.data = data

    def run(self) -> list:
        """
        将0所在的横轴和竖轴全部置零
        """
        tipRow = []
        tipCol = []
        for row, val in enumerate(self.data):
            for col, v in enumerate(val):
                if v == 0:
                    tipCol.append(col)
                    tipRow.append(row)

        for row, val in enumerate(self.data):
            for col, v in enumerate(val):
                if row in tipRow or col in tipCol:
                    self.data[row][col] = 0

        return self.data


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    res = Solution(matrix).run()
    print(res)
