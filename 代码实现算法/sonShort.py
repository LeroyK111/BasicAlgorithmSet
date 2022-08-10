#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
一串字符串中，找到不重复字符的最长子串.
逐个字符进行分割,只要每次分割的字符串小于余下的，则继续分割下去，直到最大字符串和余下字符串不满足条件后，最后判断一次。
"""


class Solution:

    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        sub = ''
        res = ''

        for i in s:
            # 最外层循环每个字符
            if i not in sub:
                # 如果字符不在sub中，则sub添加该字符
                sub += i
            else:
                # 如果在，则计算位置
                if len(res) <= len(sub):
                    # res还没加入字符
                    res = sub
                # 切割，取余下最后一个列表，然后补充一个i
                sub = sub.split(i)[-1] + i

        data = [sub, res]
        return data, max(map(lambda x: len(x), data))


if __name__ == '__main__':
    x = Solution().lengthOfLongestSubstring("sadfsdasdjlfjjlkslkdajflks")
    print(x)
