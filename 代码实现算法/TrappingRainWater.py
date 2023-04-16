#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
一层层计算间隙值，遇到图形问题，着重以图形的方法解决：分割法首选
"""


class Demo(object):

    def __init__(self, data: list) -> None:
        self.result = []
        self.data = data

    def nextRow(self):
        # 修改data，最大值减去1
        self.data = list(
            map(lambda x: x - 1 if x == self.maxNum else x, self.data))
        self.run()

    def changeData(self, maxNum):
        # 排除数量不足的情况
        maxNumCount = self.data.count(int(maxNum))
        if maxNumCount == 1:
            self.nextRow()
            return

        # 计算最高层的空缺值
        maxNumIndex = []
        strNum = "".join(map(lambda x: str(x), self.data))
        startIndex = 0
        for i in range(maxNumCount):
            index = strNum.find(maxNum, startIndex)
            maxNumIndex.append(index)
            startIndex = index + 1

        # 两两求差，只保留差值大于1的数字
        for i, value in enumerate(maxNumIndex):
            if i == len(maxNumIndex) - 1:
                break
            done = maxNumIndex[i + 1] - maxNumIndex[i] - 1
            if done >= 1:
                self.result.append(done)

        self.nextRow()

    def run(self):
        self.maxNum = max(self.data)
        if self.maxNum == 0:
            return
        self.changeData(str(self.maxNum))

    def start(self):
        self.run()
        return sum(self.result)


if __name__ == '__main__':
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [4, 2, 0, 3, 2, 5]
    D = Demo(height)
    result = D.start()
    print(result)
