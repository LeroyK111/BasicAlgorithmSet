#!/usr/bin/python
# -*- coding: utf-8 -*-


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
        # 对原始数据排序，根据每组数据的最小值，进行排序，减少计算量
        for min, max in intervals:
            key = intervals.index([min, max])
            indexs[str(key)] = min

        values = list(indexs.values())
        values.sort()
        # 判断value对应index，然后映射成列表
        newIndex = list(map(lambda x: [k for k, v in indexs.items() if x == v][0], values))
        intervals = list(map(lambda i: intervals[int(i)], newIndex))
        return intervals

    def __init__(self, intervals: list) -> None:
        self.res = []
        self.Exclusion = []
        # 初始数据处理
        self.intervals = self.sort(intervals)
        self.data = list(map(lambda x: list(range(x[0], x[1] + 1)), self.intervals))

    def count(self, data: list, index=0) -> None:
        First = data[index]

        if index + 1 >= len(data):
            # 全部推算完毕，需要重新整理
            self.res = list(map(lambda v: [min(v), max(v)], data))
            return

        Next = data[index + 1]

        if not set(First).isdisjoint(set(Next)):
            # 去除data的12项，data在index位置上插入
            data.pop(index)
            data.pop(index)
            data.insert(index, list(set(First) | set(Next)))
            self.count(data, index)
        else:
            # 修改index，索引位置向后移动
            self.count(data, index + 1)

    def run(self) -> list:
        self.count(self.data)
        return self.res


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [3, 11], [8, 10], [15, 18], [15, 18]]
    res = Demo(intervals).run()
    print(res)
