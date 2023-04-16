#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import combinations, islice, permutations


class Demo(object):

    def createMaterial(self):

        for i in range(self.n):
            # 每次循环创建n-1个列表
            data = ["." for i in range(self.n - 1)]
            # 然后在对应位置上插入Q
            data.insert(i, "Q")
            self.Material.append(data)

        # 允许空行
        # data = ["." for i in range(self.n)]
        # self.Material.append(data)

    def __init__(self, n=1) -> None:
        self.n = n
        self.Material = []
        # 生成对应的素材n种
        self.createMaterial()
        self.result = []

    def permutation(self, nativeList=[]):
        # 全排列
        data = list(permutations(nativeList, self.n))
        # 根号2
        anchor = pow(2, .5)
        # 筛选
        for value in data:
            plies = 0
            flag = 0
            changeList = []
            CoordinateVector = []
            # 每一个棋子只占有9格
            for row in value:
                try:
                    index = row.index("Q")
                except ValueError:
                    # 排除0Q的干扰
                    pass
                else:
                    # 记录矢量坐标
                    CoordinateVector.append([plies, index])
                finally:
                    # 顺便合并该行
                    changeList.append("".join(row))
                    plies += 1

            # 两两比较矢量距离，必须大于根号2，不能是根号2的倍数,不然就跳过
            ls = list(combinations(CoordinateVector, 2))
            count = len(ls)

            for d1, d2 in list(ls):
                x = pow((d1[0] - d2[0]), 2)
                y = pow((d1[1] - d2[1]), 2)
                r = pow((x + y), .5)
                if r > anchor and r % anchor != 0:
                    flag += 1
            if flag == count:
                self.result.append(changeList)

    def run(self) -> list[str]:
        if self.n == 1:
            return [["Q"]]
        elif self.n == 2:
            result = []
            data = list(set(permutations(["Q", ".", ".", "."], 4)))
            for value in data:
                result.append(["".join(value[0:2]), "".join(value[2:4])])
            return result
        # 利用素材进行全排列，并判断是否是需要的
        self.permutation(nativeList=self.Material)
        return self.result


if __name__ == '__main__':
    # 4x4矩阵中，最多放入多少个九宫格棋子
    n = 4
    A = Demo(n)
    result = A.run()
    """
    [
        [".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]
    ]
    """
    print(result)
