#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

最高位判断，左减右加原则
"""


class Solution:

    def __init__(self):
        # 直接列出所有的节点值
        self.num = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1, 0)
        self.word = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V',
                     'IV', 'I', None)

    def intToRoman(self, num: int) -> str:
        result: list[str] = []

        index: int = 0
        value: int = self.num[0]
        word: str = self.word[0]

        while num > 0:
            # Compute counter
            counter: int = num // value

            if counter == 0:
                index += 1
                value = self.num[index]
                word = self.word[index]
            else:
                # Update num
                num -= counter * value

                # Add word
                result.extend((word,) * counter)

                # Update next value
                index += 1
                value = self.num[index]
                word = self.word[index]

        return ''.join(result)


if __name__ == '__main__':
    x = Solution()
    result = x.intToRoman(299)
    print(result)
