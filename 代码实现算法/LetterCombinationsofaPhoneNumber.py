#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans_list = []

        def backtracking(idx, ans):
            if idx == len(digits):
                ans_list.append(ans)
                return
            for i in mapping[digits[idx]]:
                # 开始映射
                backtracking(idx + 1, ans + i)

        if len(digits) == 0:
            return []

        backtracking(0, '')
        return ans_list


if __name__ == '__main__':
    number = "23"
    x = Solution()
    result = x.letterCombinations(number)
    print(result)