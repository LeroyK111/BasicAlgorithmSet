#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
动态规划：

1到n连续数组，组成的二叉树方式。


dp[i]
dp[0] = 1
dp[1] = dp[0] * dp[0] + 0 = 1
dp[2] = dp[1] * 2 + 0 = 2
dp[3] = 
1为根节点 dp[2] 2
2为根节点 dp[1] 1
3为根节点 dp[2] 2

dp[4] = 
1为根节点 dp[3] 5   
2为根节点 dp[2] 2 
3为根节点 dp[2] 2
4为根节点 dp[3] 5

"""


class Solution:
    def numTrees(self, n: int) -> int:
        # n+1个树
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        # print(dp)

        for i in range(1, n + 1):
            # i 树
            for j in range(0, i):
                # 给i树赋值, 
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


if __name__ == "__main__":
    result = Solution().numTrees(4)
    print(result)
