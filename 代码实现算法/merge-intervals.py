#!/usr/bin/python
# -*- coding: utf-8 -*-

# import itertools
"""
上下限合并
"""


def demo(intervals: list) -> list:
    res = []
    # 再排除被合并的项目
    Exclusion = []
    # 区间整理
    data = list(map(lambda x: list(range(x[0], x[1] + 1)), intervals))
    # 只要区间有重复的元素>=1 我们就合并该区间的上下限数字
    for x in data:
        if x in Exclusion:
            continue
        index = data.index(x)
        if index == len(data) - 1:
            res.append([min(x), max(x)])
            break
        nextRow = data[index + 1]
        if x[-1] in nextRow:
            Exclusion.append(nextRow)
            res.append([min(x), max(nextRow)])
        else:
            res.append([min(x), max(x)])

    return res


if __name__ == '__main__':

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # [[1,6],[8,10],[15,18]]
    # intervals = [[1, 4], [4, 5]]
    res = demo(intervals)
    print(res)