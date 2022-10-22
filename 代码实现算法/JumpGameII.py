#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
跳跃游戏，中间值
"""


class Solution:

    def jump(self, nums: list[int]) -> int:
        # 长度
        n = len(nums)
        # 初始最大值1
        max_reach = nums[0]
        # 初始最小值
        end = nums[0]
        # 最小步数1
        jump = 1
        # 如果长度为0，则步数就是1
        if n == 1:
            return 0
        # 循环，从第二个值，取到倒数第二个值
        for i in range(1, n - 1):
            # 找到最大值
            max_reach = max(max_reach, i + nums[i])
            # 判断步数
            if i == end:
                end = max_reach
                jump += 1
        return jump


if __name__ == '__main__':
    A = Solution()
    result = A.jump([1, 1, 0, 1, 4])
    print(result)