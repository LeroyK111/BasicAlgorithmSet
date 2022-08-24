#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list):
    result = []
    for i in data:
        result.extend(i)
    result.sort()
    return result


if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    result = demo(lists)
    print(result)