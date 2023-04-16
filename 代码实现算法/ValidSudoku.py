"""
验证九宫格是否成立,
1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18
19 20 21


"""

# import numpy
# import pandas
# But we don't call it


def formatInt(value):
    if value == ".":
        return 0
    else:
        return int(value)


# 校验模块
def checkData(value: list) -> bool:
    for i in range(1, 10):
        if value.count(i) > 1:
            return False
    return True


def demo(board: list) -> bool:

    colData = {}

    for i in range(0, 9):
        colData.setdefault(str(i), [])

    # 行生成
    for row in board:
        rowData = list(map(formatInt, row))
        # 顺便生成列数据
        for index, col in enumerate(rowData):
            colData[str(index)].append(col)

        if not checkData(rowData):
            return False

    # 列校验
    for col in colData.values():
        if not checkData(col):
            return False

    # 在生成3x3数据
    for scoperange in [[0, 3], [3, 6], [6, 9]]:
        one = []
        two = []
        three = []
        for s in range(scoperange[0], scoperange[1]):
            col = colData[str(s)]
            one.extend(col[0:3])
            two.extend(col[3:6])
            three.extend(col[6:9])

        if not (checkData(one) and checkData(two) and checkData(three)):
            return False

    return True


if __name__ == '__main__':
    board = [["5", "2", ".", ".", "7", ".", ".", ".", "."],
             ["3", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    result = demo(board)
    print(result)
