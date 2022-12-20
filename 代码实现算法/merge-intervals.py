#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as itert

"""
合并区间
"""


class Demo(object):
    def sort(self, intervals):
        tmpe = []
        # 剔除重复数据
        intervals = [tmpe.append(x) for x in intervals if x not in tmpe]
        intervals = tmpe
        indexs = {}
        # 对原始数据排序，根据每组数据的最大值，进行排序，减少计算量
        for min, max in intervals:
            key = intervals.index([min, max])
            indexs[str(key)] = max

        values = list(indexs.values())
        values.sort()

        # 判断value对应index，然后映射成列表
        newIndex = map(lambda x: [k for k, v in indexs.items() if x == v], values)
        
        intervals = map(lambda i: intervals[i], newIndex)

        return intervals

    def __init__(self, intervals: list) -> None:
        self.res = []
        self.Exclusion = []
        # 初始数据处理
        self.intervals = self.sort(intervals)
        print(self.intervals)
        
        self.data = list(map(lambda x: list(range(x[0], x[1] + 1)), self.intervals))

    def count(self, data) -> None:
        # 挨个合并，走递归
        pass

    def run(self) -> list:
        #
        # self.count(self.data)

        return self.res


if __name__ == "__main__":
    # 这里存在一个bug,
    intervals = [[1, 3], [2, 6], [3, 7], [8, 10], [15, 18], [15, 18]]
    # [[1,6],[8,10],[15,18]]
    # intervals = [[1, 4], [4, 5]]
    res = Demo(intervals).run()

    print(res)
