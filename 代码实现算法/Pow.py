#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(num: int, p: int) -> float:
    return pow(num, p)


if __name__ == '__main__':
    num = 2
    p = 10
    result = demo(num, p)
    print(result)