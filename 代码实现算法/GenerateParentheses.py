#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
n=1 ["()"] result=1
n=2 ["()", "(())", "()()"] result=3
n=3 ["((()))","(()())","(())()","()(())","()()()"] result=5
"""


class Solution(object):

    def generateParenthesis(self, N):
        if N == 0:
            return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
