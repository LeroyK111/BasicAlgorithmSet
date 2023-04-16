#!/usr/bin/python
# -*- coding: utf-8 -*-

from MergeIntervals import Demo as MI


"""
插入区间，再合并区间。
"""


class Demo(object):
    def __init__(self, data: list, ele: list, index: int = 0) -> None:
        data.insert(index, ele)
        self.MI = MI(data)

    def run(self):
        return self.MI.run()


if __name__ == "__main__":
    data = [[1, 4], [4, 5]]
    ele = [6, 8]
    res = Demo(data, ele).run()
    print(res)
