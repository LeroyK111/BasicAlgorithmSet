#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for ii in range(1, n):
                dp[i][ii] = dp[i - 1][ii] + dp[i][ii - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    m, n = 3, 7
    res = Solution().uniquePaths(m, n)
    print(res)
