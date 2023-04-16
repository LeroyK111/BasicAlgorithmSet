#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def run(self, nums1: list, nums2: list, m: int, n: int):
        data = [*nums1[0:m], *nums2[0:n]]

        data.sort()
        return data


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    result = Solution().run(nums1, nums2, m, n)
    print(result)
