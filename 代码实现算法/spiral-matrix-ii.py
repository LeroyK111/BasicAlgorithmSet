#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
给你一个正整数 n ，生成一个包含 1 到 n平方 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
"""


class Demo(object):
    def __init__(self, data) -> None:
        self.data = data

        self.result = []

    # right down left up 循环方向
    def count(self, data: list, flag="right"):
        match flag:
            case "right":
                
                
                self.count(data, "down")
            case "down":
                print(1)
                self.count(data, "left")

            case "left":
                print(1)
                self.count(data, "up")

            case "up":
                print("1")
                self.count(data, "right")

    def run(self):
        self.count(data=self.data)
        return self.result


if __name__ == "__main__":
    # 先不考虑特殊数据，直接计算顺时针螺旋
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Demo(data).run()
    print(result)
