#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
? 匹配单个任意字符
* 匹配任意数量的字符，包括空字符
"""


class Demo(object):

    def __init__(self, restr: str, data: str) -> None:
        self.restr = restr
        self.data = data
        self.ones = restr.count("?")
        self.anys = restr.count("*")

    def checkStr(self, newStr: list, data: str):
        for i in newStr:
            if data.find(i) == -1:
                return False
        return True

    def run(self):
        if self.restr == self.data:
            return True

        if self.ones > 0 and self.anys == 0 and len(self.data) == len(
                self.restr):
            # 对？进行处理
            newStr = self.restr.split("?")
            return self.checkStr(newStr, self.data)
        elif self.anys > 0 and self.ones == 0:
            # 对*进行处理
            newStr = self.restr.split("*")
            return self.checkStr(newStr, self.data)
        else:
            # 先切割*
            starlist = self.restr.split("*")
            # 再切割？
            for data in starlist:
                newStr = data.split("?")
                return self.checkStr(newStr, data)
        return False


if __name__ == '__main__':
    restr = "*s?2"
    data = "ababs22"
    A = Demo(restr, data)
    result = A.run()
    print(result)