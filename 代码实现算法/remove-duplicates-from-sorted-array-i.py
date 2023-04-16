#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def run(self, data: list) -> list:
        result = []
        for i in set(data):
            n = data.count(i)
            if n > 2:
                n = 2
            result.extend([i] * n)

        return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    result = Solution().run(nums)
    print(result)
