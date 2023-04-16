#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


def demo2(a, b, strs):
    # 排列
    for index, ele in enumerate(strs):
        b += ele
        if index == a - 1:
            strs = strs[index + 1:]
            return b, strs


def demo(strs: str, numRows: int) -> str:
    strs = list(strs.upper())
    if numRows == 1:
        return strs
    """
    不用numpy的矩阵思维，使用普通函数实现：
    每一行元素数量相同，数量不足的行用空格补足
    """
    a = math.ceil(len(strs) / numRows)
    b = ""

    for i in range(numRows):
        # 换行
        if i != 0:
            b += "\n"

        # 最后一行缺失问题
        if len(strs) < a:
            space = a - len(strs)
            for s in range(space):
                strs += " "

        b, strs = demo2(a, b, strs)

    print(b)


if __name__ == '__main__':
    print(len("sldkajlkewrcxuass"))
    demo(strs="sldkajlkewrcxuass", numRows=4)
