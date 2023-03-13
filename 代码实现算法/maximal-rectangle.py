#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def maximalRectangle(self, matrix: list[str]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0
            # print(pre)

            # 单调栈
            stack = [-1]
            for k, num in enumerate(pre):
                # print(k, num)
                while stack and pre[stack[-1]] > num:
                    # print(stack, num, pre[stack[-1]])
                    index = stack.pop()
                    res = max(res, pre[index] * (k - stack[-1] - 1))
                
                stack.append(k)

        return res


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    result = Solution().maximalRectangle(matrix)
    print(result)
