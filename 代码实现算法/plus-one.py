#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list) -> list:
    data[-1] += 1
    
    
    return data


if __name__ == "__main__":
    digits = [1, 2, 3]
    res = demo(digits)
    print(res)
