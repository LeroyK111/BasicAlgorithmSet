#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):

    def combinationSum(self, candidates, target):
        # 接收参数
        ret = []
        # 调用方法，传入参数，最后把参数传出
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        """
        递归循环，
        """
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
