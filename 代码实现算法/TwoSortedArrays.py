#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(nums1, nums2):
    # 合并列表，并排序
    df = nums1 + nums2
    df.sort()

    # 取中位数
    if len(df) % 2 != 0:
        # 奇数
        return df[int((len(df) - 1) / 2)]
    else:
        # 偶数
        a = df[int(len(df) / 2 - 1)] + df[int(len(df) / 2 + 1)]
        return a / 2


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 3], [2, 3, 1, 2]
    result = demo(nums1, nums2)
    print("中位数是", result)
