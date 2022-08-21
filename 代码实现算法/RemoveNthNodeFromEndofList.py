#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list, n: int) -> list[int]:
    data.pop(len(data) - n)
    return data


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    n = 2
    result = demo(head, n)
    print(result)