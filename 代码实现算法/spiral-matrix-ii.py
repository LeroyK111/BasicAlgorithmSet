#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
给你一个正整数 n ，生成一个包含 1 到 n平方 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
"""


class Demo(object):
    def __init__(self, data) -> None:
        self.matrix = data

    # right down left up 循环方向
    def run(self) -> list:
        """
        动态边界法：
        第一次循环，1 1 1 1
        第二次循环，2 1 1 1 跳出循环
        """
        res = []
        if self.matrix is None:
            # 避免空值
            return res

        # !设定四个边界,            top=0    bottom=2        left=0    right=2
        top, bottom, left, right = 0, len(self.matrix) - 1, 0, len(self.matrix[0]) - 1
        while True:
            for i in range(left, right + 1):  # ➡️ 从左至右
                res.append(self.matrix[top][i])
            top += 1  # 上边减去1
            if top > bottom:
                # 避免超越边界
                break
            for i in range(top, bottom + 1):  # ⬇️ 从上至下
                res.append(self.matrix[i][right])
            right -= 1  # 右边减去1
            if right < left:
                # 避免越过边界
                break
            for i in range(right, left - 1, -1):  # ⬅️ 从右往左 1 -1 -1 = 1 0
                res.append(self.matrix[bottom][i])
            bottom -= 1  # 下边减去1
            if bottom < top:
                # 避免越过边界
                break
            for i in range(bottom, top - 1, -1):  # ⬆️ 从下至上 1 0 -1 = 1
                res.append(self.matrix[i][left])
            left += 1  # 左边减去1
            if left > right:
                # 避免越过边界
                break
        return res


if __name__ == "__main__":
    # 先不考虑特殊数据，直接计算顺时针螺旋
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Demo(data).run()
    print(result)
