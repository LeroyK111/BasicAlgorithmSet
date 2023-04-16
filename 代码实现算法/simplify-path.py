#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


class Solution(object):
    def __init__(self, path: str) -> None:
        self.path = path

    def run(self):
        res = os.path.normpath(self.path)
        return res


if __name__ == "__main__":
    path = "/home/"
    path = "/home//foo/"
    path = "/a/./b/../../c/"
    res = Solution(path=path).run()
    print(res)
