#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
线性阶
"""


class Solution(object):
    def run(self, head: list, left: int, right: int) -> list:
        left -= 1
        cutHead = head[left:right]
        for i in cutHead:
            head.remove(i)
            head.insert(left, i)

        return head


if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    result = Solution().run(head, left, right)
    print(result)
