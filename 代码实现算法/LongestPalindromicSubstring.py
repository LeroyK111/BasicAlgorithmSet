#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
找相同字符包裹的最长子串。
以下过程还可以继续优化，我就不做探究了.
"""


def demo(strs: str) -> str:
    maxStr = ""
    itemStr = ""
    for i in strs:
        flag = 1

        # 直接把次数小于1的剔除掉
        if strs.count(i) <= 1:
            continue

        data = strs.split(i)


        
        if data[0] == "":
            flag = 0
        if data[-1] == "":
            flag = -1
        if data[-1] == data[0] == "":
            flag = 2

        itemStr = data[0]

        for item in data:
            if len(item) > len(itemStr):
                """
                判断是不是真的处于i + item + i 之间
                """
                match flag:
                    case 1:
                        # 去掉首尾两组元素
                        if item == data[-1] or item == data[0]:
                            pass
                        else:
                            itemStr = i + item + i
                    case 0:
                        # 去掉尾元素
                        if item == data[-1]:
                            pass
                        else:
                            itemStr = i + item + i
                    case -1:
                        # 去掉首元素
                        if item == data[0]:
                            pass
                        else:
                            itemStr = i + item + i
                    case 2:
                        # 
                        itemStr = i + item + i


        if len(maxStr) < len(itemStr):
            maxStr = itemStr

    return maxStr


if __name__ == '__main__':
    strs = "sdlfjlkwjriuvnnvmzkwwqro"
    maxStr = demo(strs)
    print(maxStr)