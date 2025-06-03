#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
自下而上的迭代；
"""


def mergeSort(arr):
    import math
    if (len(arr) < 2):
        return arr
    # 向下取整
    middle = math.floor(len(arr) / 2)
    # 列表切割
    left, right = arr[0:middle], arr[middle:]
    print("left:", left, "right:", right)
    # 调用下一个方法
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    # 当两组列表都存在时
    while left and right:
        print(result)
        # 各自判断个列表首个元素的大小
        if left[0] <= right[0]:
            # left弹出这个元素，
            result.append(left.pop(0))
        else:
            # right弹出这个元素
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    arr = mergeSort(arr=[3, 2, 7, 1])
    print(arr)
