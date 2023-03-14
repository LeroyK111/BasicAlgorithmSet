#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as it


class Solution(object):
    def run(self, a: str, b: str) -> bool:
        seed = map("".join, it.permutations(a))
        for i in seed:
            if i.find(b) != -1:
                return True

        return False


if __name__ == "__main__":
    s1 = "great"
    s2 = "rgeat"
    result = Solution().run(s1, s2)
    print(result)
