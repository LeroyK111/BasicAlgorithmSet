#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as it


class Solution:
    def run(self, nums: list[int]):
        result = []
        for i in range(len(nums) + 1):
            d = list(set(it.permutations(nums, i)))
            y = []
            for x in d:
                x = list(x)
                x.sort()
                if x not in y:
                    y.append(x)
            result.append(y)

        return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    result = Solution().run(nums)
    print(result)
