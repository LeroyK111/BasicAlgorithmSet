#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def run(self, data: list):
        return list(filter(lambda x: x is not None, data))


if __name__ == "__main__":
    root = [1, None, 2, 3]
    result = Demo().run(root)
    print(result)
