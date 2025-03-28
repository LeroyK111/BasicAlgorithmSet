"""
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

1. 基数排序 vs 计数排序 vs 桶排序
基数排序有两种方法：

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：

基数排序：根据键值的每位数字来分配桶；
计数排序：每个桶只存储单一键值；
桶排序：每个桶存储一定范围的数值；
"""


def demo(arr):
    data = {}
    for item in arr:
        # 手动分桶
        if data.get(str(len(str(item)))) is None:
            data["%s" % len(str(item))] = []
        data["%s" % len(str(item))].append(item)

    # 桶分完,然后对各个桶进行排序,然后逐个拼接
    new_arr = []
    for _, value in data.items():
        value.sort(reverse=False)
        new_arr.extend(value)
    return new_arr


if __name__ == '__main__':
    arr = demo([2, 3, 11, 5, 16, 2, 3, 12])
    print(arr)
