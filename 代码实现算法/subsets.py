#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools as it


class Solution(object):
    def demo(self, nums: list):
        result = []
        for i in range(len(nums) + 1):
            d = it.combinations(nums, i)
            result.extend(d)

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    res = Solution().demo(nums)
    print(res)
