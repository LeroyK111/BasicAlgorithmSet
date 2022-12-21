#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: str) -> int:

    return len(data.split()[-1])


if __name__ == "__main__":
    data = "hello is   world"
    res = demo(data)
    print(res)
