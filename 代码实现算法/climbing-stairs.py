#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
# 只依赖前两阶梯状态
1 1种
2 2种
3 3中
4 5种
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]表示爬到第i级楼梯的种数， (1, 2) (2, 1)是两种不同的类型
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for j in range(1, 3):
                if i >= j:
                    dp[i] += dp[i - j]
        return dp[-1]


if __name__ == "__main__":
    num = 10
    result = Solution().climbStairs(num)
    print(result)
