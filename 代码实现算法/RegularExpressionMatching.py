#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
手搓正则表达式
'.'点匹配一个任意字符
'*'匹配任意数量的字符
需要考虑多种情况，.*重复的情况


"""


def checkKong(i):

    if len(i) > 0:
        return i


def listDr(data: list):
    newData = []
    for i in data:
        newData.extend(i)

    return newData


def demo(data: str, re: str) -> bool:
    dotNum = re.count(".")
    starNum = re.count("*")

    if dotNum == 0 and starNum == 0:
        return True if data == re else False

    if dotNum > 0 and starNum == 0:
        if len(re) != len(data):
            # 排除字符干扰
            return False

        dotList = re.split(".")

        l1 = filter(checkKong, dotList)
        # 利用find的特性，寻找全部的子串，只要有一个子串找不到，那就返回False,否则返回True
        for i in l1:
            if data.find(i) == -1:
                return False
        return True

    if starNum > 0 and dotNum == 0:
        starList = re.split("*")
        l1 = filter(checkKong, starList)
        # 利用find的特性，寻找全部的子串，只要有一个子串找不到，那就返回False,否则返回True
        for i in l1:
            if data.find(i) == -1:
                return False
        return True

    if starNum > 0 and dotNum > 0:
        # 需要同时切片两个字符
        dotList = re.split(".")
        dotStarList = list(map(lambda x: x.split("*"), dotList))
        # 直接将二维数组降维到一维去
        newData = listDr(dotStarList)
        # 去空
        l1 = filter(checkKong, newData)
        for i in l1:
            if data.find(i) == -1:
                return False
        return True


if __name__ == '__main__':
    data = "aa"
    re = "asdfdsewr.a*asjdlfker."
    result = demo(data, re)
    print(result)
