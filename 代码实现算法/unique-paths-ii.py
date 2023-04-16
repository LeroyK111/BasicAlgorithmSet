"""
右下角越过一个障碍物到达左上角

x 0 0
0 y 0
0 0 s
"""

import itertools as it


class Demo(object):
    def __init__(self, obstacleGrid: list) -> None:
        self.obstacleGrid = obstacleGrid
        self.result = 0
        self.stoneIndex = self.findYIndex()
        self.data = []

    def findYIndex(self):
        for i in range(len(self.obstacleGrid)):
            for j in range(len(self.obstacleGrid[0])):
                if self.obstacleGrid[i][j] == 1:
                    return [i, j]

    def allPaths(self):
        width = len(self.obstacleGrid[0]) - 1
        height = len(self.obstacleGrid) - 1
        self.start = [width, height]
        # 最简步数
        leftSteps = width * ["left"]
        upSteps = height * ["up"]
        allsteps = [*leftSteps, *upSteps]
        # 步骤全排列
        steps = set(it.permutations(allsteps, len(allsteps)))
        # 将步骤映射成点位坐标
        newSteps = []
        for s in steps:
            start = self.start
            for j in s:
                if j == "up":
                    row = start[0] - 1
                    start = index = [row, start[1]]
                    newSteps.append(index)
                elif j == "left":
                    col = start[1] - 1
                    start = index = [start[0], col]
                    newSteps.append(index)
        # 拆分
        a = len(allsteps)
        for i in range(int(len(newSteps) / a)):
            start = i * a
            end = start + a
            self.data.append(newSteps[start:end])

    def fillter(self):
        res = []
        for i in self.data:
            if self.stoneIndex not in i:
                res.append(i)

        return res

    def count(self) -> int:
        if len(self.obstacleGrid) == 0:
            return self.result

        # 找到所有的路径组合
        self.allPaths()
        # 剔除含有y的路径组合
        res = self.fillter()

        # 计算无障碍的路径组合数
        return len(res)


if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    D = Demo(obstacleGrid)
    res = D.count()
    print(res)
