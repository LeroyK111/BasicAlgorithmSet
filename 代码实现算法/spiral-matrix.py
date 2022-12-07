#!/usr/bin/python
# -*- coding: utf-8 -*-


class Example(object):

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    """
    动态边界法
    """

    def run(self) -> list:
        res = []
        if self.matrix is None:
            return res
        top, bottom, left, right = 0, len(self.matrix) - 1, 0, len(
            self.matrix[0]) - 1
        while True:
            for i in range(left, right + 1):  #➡️
                res.append(self.matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):  #⬇️
                res.append(self.matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):  #⬅️
                res.append(self.matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            for i in range(bottom, top - 1, -1):  #⬆️
                res.append(self.matrix[i][left])
            left += 1
            if left > right:
                break
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # [1,2,3,6,9,8,7,4,5]
    # self.matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # [1,2,3,4,8,12,11,10,9,5,6,7]
    demo = Example(matrix)
    result = demo.run()
    print(result)