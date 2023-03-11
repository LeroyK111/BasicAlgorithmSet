#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def countArea(self, target: int):
        # 以target为界，从小于target地方拆分数组
        strs = "".join(map(str, self.height))
        # 找出小于target的数字
        data = list(filter(lambda x: x < target, self.height))

        if len(data) == 0:
            area = len(strs) * target
            if area > self.area:
                self.area = area
            return

        # 拆分
        for i in data:
            ss = strs.split(str(i))
            for s in ss:
                s = list(filter(lambda x: int(x) >= target, s))
                area = len(s) * target
                if area > self.area:
                    self.area = area

    def run(self, heights: list) -> int:
        # 贪心算法，从最矮的开始算矩形
        self.area = 0
        self.height = heights
        data = list(set(heights))
        data.sort()
        for i in data:
            self.countArea(i)

        return self.area


if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    result = Solution().run(heights)
    print(result)
