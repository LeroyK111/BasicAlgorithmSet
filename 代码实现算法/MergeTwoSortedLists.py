#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(list1: list, list2: list):
    list1.extend(list2)
    list1.sort()
    return list1


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    result = demo(list1, list2)
    print(result)