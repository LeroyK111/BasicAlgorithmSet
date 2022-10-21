#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(a, b) -> str:
    a, b = float(a), float(b)
    return str(a * b)


if __name__ == '__main__':
    a = "222"
    b = "333"
    result = demo(a, b)
    print(result)