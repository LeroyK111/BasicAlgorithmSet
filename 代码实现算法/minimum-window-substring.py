#!/usr/bin/python
# -*- coding: utf-8 -*-

import random as rand


class Solution:
    def __init__(self, s: str, t: str) -> None:
        self.s = s
        self.t = t
        self.res = []

    def createIndexList(self, data):
        if data[1] == self.i:
            return data[0]

    def minimumDifference(self, indexs):
        result = max(indexs) - min(indexs)
        return result

    def fullPermutation(self, data, count):
        ls = []
        while True:
            d = []
            for va1 in data:
                va2 = rand.choice(va1)
                d.append(va2)
            if d not in ls:
                ls.append(d)
            if len(ls) == count:
                s = list(map(self.minimumDifference, ls))
                i = s.index(min(s))
                self.res = self.s[min(ls[i]) : max(ls[i]) + 1]
                return

    def run(self):
        """
        思路：
        1.按照子串的每个字符进行索引归纳
        2.每个字符的位置抽取一个,进行全排列
        3.坐标组最大值和最小值相差最小的就是最近子串的一组坐标
        4.坐标转字符，返回即可
        """
        if len(self.s) < len(self.t):
            return ""

        ls = []
        for i in self.t:
            self.i = i

            if self.s.find(i) == -1:
                return ""

            data = list(filter(lambda x: x is not None, map(self.createIndexList, enumerate(self.s))))
            ls.append(data)

        s = map(lambda x: len(x), ls)
        nums = 1
        for i in s:
            nums *= i

        self.fullPermutation(data=ls, count=nums)

        return self.res


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution(s, t).run()
    print(result)
