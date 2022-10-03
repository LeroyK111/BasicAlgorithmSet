#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):

    def combinationSum(self, candidates: list, target: int):
        self.checkCount = {}
        # 计算里面每个元素的数量
        for i in set(candidates):
            self.checkCount[str(i)] = candidates.count(i)

        # 接收参数
        ret = []
        # 调用方法，传入参数，最后把参数传出
        self.dfs(candidates, target, [], ret)
        return ret

    def dfs(self, nums, target, path, ret):
        if target < 0:
            return
        if target == 0:
            # 加入过滤
            data = list(
                map(
                    lambda x: True
                    if path.count(x) == self.checkCount[str(x)] else False,
                    set(path)))
            if data.count(False) != 0:
                return
            ret.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], ret)


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    demo = Solution()
    result = demo.combinationSum(candidates, target)
    print(result)
