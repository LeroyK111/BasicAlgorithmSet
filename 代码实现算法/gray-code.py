#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as it


class Solution(object):
    def run(self, n: int):
        data = []
        for i in range(2**n):
            data.append(i)

        data = list(map(bin, data))

        # 全排列
        data = it.permutations(data)
        for i in data:
            flag = 0
            max = len(i)
            for index, value in enumerate(i):
                nextIndex = index + 1
                if nextIndex == max:
                    nextIndex = 0
                if value != i[nextIndex]:
                    flag += 1
                if flag == 4:
                    # 转换回十进制数
                    return list(map(lambda x: int(x, 2), i))


if __name__ == "__main__":
    n = 2
    result = Solution().run(n)
    print(result)
