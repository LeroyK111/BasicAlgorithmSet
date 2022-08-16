#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(data: list) -> dict:
    result = {"size": 0, "ele1": None, "ele2": None}
    # 使用索引和高度，当成面积计算公式
    for index1, ele1 in enumerate(data):
        for index2, ele2 in enumerate(data):
            D = abs(index2 - index1)
            minHeight = min([ele1, ele2])
            size = D * minHeight
            if size > result["size"]:
                result["size"] = size
                result["ele1"] = (ele1, index1)
                result["ele2"] = (ele2, index2)
    return result


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = demo(height)
    print(result)