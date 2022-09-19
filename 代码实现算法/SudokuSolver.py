#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from ValidSudoku import demo as checkSudoku


def format(value):
    if value == ".":
        return 0
    else:
        return int(value)


def demo(board: list) -> list:
    while True:
        data = []
        # 使用满足条件随机数填补.
        for row in board:
            newRow = []
            row = list(map(format, row))

            # 计算每行缺失数据列表，求差集
            cha = list(set(range(1, 10)) - set(row))

            # 计算每行缺失的数据
            for value in row:
                if value == 0:
                    # 随机从缺失列表中取值，取值后在剔除列表，添加给newRow
                    s = np.random.choice(cha)
                    cha.remove(s)
                    newRow.append(s)
                else:
                    newRow.append(value)

            data.append(newRow)

        if checkSudoku(data):
            return data


if __name__ == '__main__':
    board = [["5", "2", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = demo(board)
    print(result)
