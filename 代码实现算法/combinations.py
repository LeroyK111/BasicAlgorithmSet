#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as it


class Solution:
    def __init__(self, n, k) -> None:
        self.n = n
        self.k = k

    def publish(
        self,
    ):
        """
        n: [1,n]的范围
        k：选取k个数的组合
        """
        data = list(it.permutations([i for i in range(1, n + 1)], k))
        # 剔除重复项目
        result = []
        for i in data:
            if i not in result and (i[1], i[0]) not in result:
                result.append(i)

        return result


if __name__ == "__main__":
    n = 4
    k = 2
    res = Solution(n, k).publish()
    print(res)
