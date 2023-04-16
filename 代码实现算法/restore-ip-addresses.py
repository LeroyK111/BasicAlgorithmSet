#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from random import choices


class Solution:
    def fli(self, i: str):
        ils = i.split(".")
        for d in ils:
            if d[0] != "0" and int(d) <= 255:
                return True
            else:
                return False

    def run(self, mask: str):
        data = []
        n = len(mask)
        if n < 4:
            return data

        # 总的组合数 = len(mask)-1个插槽，放入三个点
        m = 3
        # n->m的累乘 / m的累乘法
        count = math.prod(range(m, n)) / math.factorial(m)
        print(count)
        data = []
        xl = list(range(1, n))
        while True:
            # 去重
            data = list(set(data))
            if len(data) == count:
                break
            pointsIndex = choices(xl, k=m)
            for i in pointsIndex:
                x = list(mask)
                x.insert(i, ".")
            x = "".join(x)
            data.append(x)

        data = list(filter(self.fli, data))

        return data


if __name__ == "__main__":
    mask = "25525511135"
    result = Solution().run(mask)
    print(result)
