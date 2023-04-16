#!/usr/bin/python
# -*- coding: utf-8 -*-
import itertools as iter


class Demo(object):
    def CreateData(self):
        if self.n == 1:
            self.data = ["1"]
        elif self.n < 1:
            self.data = ["n不能小于1"]
        else:
            self.data = "".join([str(x) for x in range(1, self.n + 1)])

    def __init__(self, n=2, k=0) -> None:
        self.n = n
        self.k = k

    def run(self):
        # 创建序列
        self.CreateData()
        # 全排列，不可重复
        data = list(iter.permutations(self.data, self.n))
        return "".join(data[self.k])


if __name__ == "__main__":
    result = Demo(2, 0).run()
    print(result)
