#!/usr/bin/python
# -*- coding: utf-8 -*-


def subData(start, end, data, kong):
    if len(kong) != 0:
        return
    startIndex = data.find(start)
    endIndex = data.find(end)
    if [startIndex, endIndex].count(-1) == 1:
        kong.append(-1)

    if startIndex != -1 and endIndex != -1:
        if startIndex > endIndex:
            kong.append(-1)

        data = data.replace(start, "", 1).replace(end, "", 1)
        subData(start, end, data, kong)


def demo(data: str):

    key = {"1": ["(", ")"], "2": ["[", "]"], "3": ["{", "}"]}

    for i in key.keys():
        a = data
        kong = []
        start = key[i][0]
        end = key[i][1]
        if data.count(start) != data.count(end):
            return False
        subData(start, end, a, kong)
        if len(kong) != 0:
            return False
    return True


if __name__ == '__main__':
    data = "()[]{}"
    result = demo(data)
    print(result)
