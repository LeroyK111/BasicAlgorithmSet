"""
验证九宫格是否成立,
1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18
19 20 21


"""

# import numpy
# import pandas
# But we don't call it


def demo(board: list) -> bool:
    nativeData = range(1, 10)
    ls = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }
    # 先判断行列有没有重复
    for ele in nativeData:
        for row in board:
            if row.count(str(ele)) > 1:
                return False

            if len(ls["9"]) != 9:
                for i in range(1, 10):
                    ls[str(i)].append(row[i - 1])

    for kes in ls.keys():
        for ele in nativeData:
            if ls[kes].count(str(ele)) > 1:
                return False

    result = []
    count = 0

    # 再判断3x3格子有没有重复
    for row in board:
        result.extend([row[0:3], row[3:6], row[6:9]])
        count += 1
        if count == 3:
            for i in range(3):
                data = []
                data.extend(result[i])
                data.extend(result[i + 3])
                data.extend(result[i + 6])
                for ele in nativeData:
                    if data.count(str(ele)) > 1:
                        return False
            result = []
            count = 0

    return True


if __name__ == '__main__':
    board = [["5", "2", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = demo(board)
    print(result)
