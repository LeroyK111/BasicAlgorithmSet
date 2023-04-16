#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def run(self, head: list, x: int) -> list:
        strList = "".join(map(str, head))
        first, later = strList.split(str(x))
        # 前提，分割项只有一个
        result = [x]
        for i in first:
            i = int(i)
            if x > i:
                result.insert(0, i)
            else:
                result.insert(1, i)
        for i in later:
            i = int(i)
            if x > i:
                result.insert(1, i)
            else:
                result.append(i)

        return result


if __name__ == "__main__":
    head = [1, 4, 3, 2, 5, 2, 4]
    x = 3
    result = Solution().run(head, x)
    print(result)
