#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(a: bin, b: bin) -> bin:
    return bin(a + b)


if __name__ == "__main__":
    # a = "11", b = "1"
    a = 0b11
    b = 0b1
    result = demo(a, b)
    print(result)
