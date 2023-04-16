import itertools as it


class Demo(object):
    def __init__(self, obstacleGrid: list) -> None:
        self.data = []
        self.obstacleGrid = obstacleGrid

    def allPaths(self):
        width = len(self.obstacleGrid[0]) - 1
        height = len(self.obstacleGrid) - 1
        self.start = [width, height]
        # 初始点值
        self.startValue = self.obstacleGrid[self.start[0]][self.start[1]]
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

    def run(self):
        self.allPaths()

        # 将self.data进行坐标映射成值，再计算。
        ress = []
        for d in self.data:
            a = sum(map(lambda i: self.obstacleGrid[i[0]][i[1]], d), self.startValue)
            ress.append(a)

        return min(ress)


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    """
    [
     [1, 3, 1], 
     [1, 5, 1], 
     [4, 2, 1]
    ]
    """
    res = Demo(grid).run()
    print(res)
