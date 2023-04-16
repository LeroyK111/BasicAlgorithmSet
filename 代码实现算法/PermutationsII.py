#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
可重复数组
"""


class Solution:

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        visited = [False] * len(nums)

        nums.sort()

        def backtracking(nums, res):
            # GOAL / Base case
            if len(res) == n:
                ans.append(res[:])
                return

            for i in range(len(nums)):
                # CONSTRAINTs
                # if current element is duplicated of previous one
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and
                                  not visited[i - 1]):
                    continue

                # Make CHOICE
                res.append(nums[i])

                # BACKTRACKING
                visited[i] = True
                backtracking(nums, res)

                # RESET STATE
                visited[i] = False
                res.pop()


# Inital state

        backtracking(nums, [])
        return ans

if __name__ == '__main__':
    A = Solution()
    res = A.permuteUnique([1, 1, 2, 3])
    print(res)
