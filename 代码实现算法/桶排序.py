"""
桶排序: 对计数排序进行了优化,先将数据离散化(分桶),然后对每个桶的内容进行排序.然后按照桶的范围依次相加.
"""

import pandas as pd


def demo(arr):
    # 列表数据离散化
    dt = pd.Series(arr)
    dt_cut = pd.cut(
        x=dt,
        bins=3,
    )
    print(dt_cut)
    # 提取桶的元素,并且直接排序
    dt = dt.groupby(dt_cut).value_counts(sort=False, ascending=True)
    # 构建新矩阵
    data = pd.DataFrame({
        "value": [i[1] for i in dt.index],
        "weight": dt.values
    })

    # 直接写入新数据
    new_arr = []
    for i in data.index:
        new_arr.extend([data.loc[i, "value"]] * data.loc[i, "weight"])
    return new_arr


if __name__ == '__main__':
    arr = demo([2, 3, 1, 5, 6, 2, 3, 12])
    print(arr)
