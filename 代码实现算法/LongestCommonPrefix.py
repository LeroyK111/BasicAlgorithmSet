#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
找到全部的公共前缀
"""


def demo(data: list) -> bool:
    result = False
    done = []

    # 找到里面字符最少的元素
    Strs = list(map(lambda x: len(x), data))
    minStr = data[Strs.index(min(Strs))]

    for i in range(len(minStr), 0, -1):
        if i - 1 == 0:
            pr = minStr[0]
        else:
            pr = minStr[0:i]

        y = 0
        for item in data:
            x = item.find(pr)
            if x != 0:
                y += 1
        if y == 0:
            done.append(pr)

    # 有多少组前缀
    print(done)

    if len(done) > 0:
        result = True

    return result


if __name__ == '__main__':
    data = ["abs", "abs23123", "absafwerijaskldj"]
    result = demo(data)
    print(result)
