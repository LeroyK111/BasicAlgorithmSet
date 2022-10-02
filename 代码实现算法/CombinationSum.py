#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):

    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    demo = Solution()
    result = demo.combinationSum(candidates, target)
    print(result)
