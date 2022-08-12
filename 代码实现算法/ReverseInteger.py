#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
反转数字，保留符号
"""


def demo(num):
    # 将符号和数字，拆开
    d = list(str(num))
    d.reverse()
    if num >= 0:
        return int("".join(d))
    else:
        d = d[:-1]
        d.insert(0, "-")
        return int("".join(d))


if __name__ == '__main__':
    num = -140
    result = demo(num)
    print(result)
