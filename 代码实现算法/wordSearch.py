#!/usr/bin/python
# -*- coding: utf-8 -*-


class Demo(object):
    def searchPath(self, StartPath: list) -> dict:
        # 0-2
        maxRow = len(self.board) - 1
        # 0-3
        maxCol = len(self.board[0]) - 1
        X = StartPath[0]
        Y = StartPath[1]
        strs = [self.board[X][Y]]
        count = 0
        oldFlag = ""
        while True:
            if "".join(strs) == self.word:
                return {"status": True, "path": strs}
            # 每循环一次列出周围四个值, 找到符合条件
            nextValue = self.word[len(strs)]
            count += 1

            if len(strs) != count:
                return {"status": False}

            if X - 1 >= 0 and oldFlag != "down":
                up = self.board[X - 1][Y]
                if up == nextValue:
                    X -= 1
                    strs.append(up)
                    oldFlag = "up"
                    continue

            if X + 1 <= maxRow and oldFlag != "up":
                down = self.board[X + 1][Y]
                if down == nextValue:
                    X += 1
                    strs.append(down)
                    oldFlag = "down"
                    continue

            if Y - 1 >= 0 and oldFlag != "right":
                left = self.board[X][Y - 1]
                if left == nextValue:
                    Y -= 1
                    strs.append(left)
                    oldFlag = "left"
                    continue

            if Y + 1 <= maxCol and oldFlag != "left":
                right = self.board[X][Y + 1]
                if right == nextValue:
                    Y += 1
                    strs.append(right)
                    oldFlag = "right"
                    continue

    def run(self, board: list, word: str) -> bool:
        # 先找word首字母坐标
        self.word = word
        self.board = board
        first = word[0]
        firstIndex = []
        for row, rowValue in enumerate(board):
            if first in rowValue:
                firstIndex.append([row, rowValue.index(first)])
        results = list(map(self.searchPath, firstIndex))
        print(results)
        for result in results:
            if result['status']:
                
                return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # mxn矩阵，搜索子串
    result = Demo().run(board, word)
    print(result)
