#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self, word1: str, word2: str) -> None:
        self.word1 = word1
        self.word2 = word2
        self.minStep = 0
        self.data = [None for _ in range(len(word1))]

    def findSmallestModification(self):
        """
        word1转换成word2的最少操作次数，无需具体操作步骤。
        插入一个字符,删除一个字符,替换一个字符.
        !只对一个字符进行操作
        """
        if self.word1 == self.word2:
            self.minStep = -1
        else:
            start = 0
            for index, value in enumerate(self.word2):
                res = self.word1.find(value, start)
                if res != -1:
                    start = res
                    self.data[start] = value
            # print(self.data)
            self.minStep = self.data.count(None)
            
    def isNum(self) -> int:
        self.findSmallestModification()
        if self.minStep == -1:
            return 0
        return self.minStep


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    demo = Solution(word1, word2)
    res = demo.isNum()
    print(res)
