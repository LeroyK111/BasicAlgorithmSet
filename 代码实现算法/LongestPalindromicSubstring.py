#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
找相同字符包裹的最长子串。
"""

itemStr = {}
sameCharacter = []
res = []


def demo2(strs, index, el, maxStr=""):
    seond_index = strs.find(el, (index + 1))
    if seond_index == -1:
        for value in itemStr[el]:
            # 把最长那组返回回来
            if len(value) > len(maxStr):
                maxStr = value
                s = (maxStr, el, len(maxStr))
        return s

    itemStr[el].append((strs[index:seond_index] + el))
    return demo2(strs, seond_index, el)


def demo(strs: str):
    for index, el in enumerate(strs):
        if strs.count(el) == 1:
            sameCharacter.append(el)
            continue
        if el not in sameCharacter:
            itemStr[str(el)] = []
            result = demo2(strs, index, el)
            res.append(result)
            sameCharacter.append(el)
    # [('abssba', 'a', 6), ('bssb', 'b', 4), ('ss', 's', 2)]
    # return res
    """
    写个冒泡算法，计算完毕
    """

    b = 0
    a = res[b][2]
    for i, value in enumerate(res):
        if a < value[2]:
            a = value[2]
            b = i

    done = res[b][0]

    return done


if __name__ == '__main__':
    strs = "abssbaasdfsadewwqweiorkldiufwqenebiuahjfwqoiuvhbaket"
    done = demo(strs)
    print(done)
