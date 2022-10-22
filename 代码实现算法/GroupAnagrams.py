#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(strs: list[str]) -> list:
    # 直接拆解
    data = []
    for value in strs:
        a = list(value)
        a.sort()
        if a not in data:
            data.append(a)

    result = {}

    # 直接分拣
    for c in data:
        key = "".join(c)
        result[key] = []
        for i in strs:
            d = list(i)
            d.sort()
            d = "".join(d)
            if d == key:
                result[key].append(i)

    result = list(result.values())

    return result


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = demo(strs)
    print(result)
