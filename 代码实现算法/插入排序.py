"""
插入排序: 双循环, 不过是从后往前排列，
"""


def insertionSort(arr):
    for i in range(len(arr)):
        # 默认索引
        preIndex = i - 1
        # 选择值
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            # 排除-1的可能，并且前一个数比后一个数大
            arr[preIndex + 1] = arr[preIndex]  # 把前一个数赋值给后一个数
            preIndex -= 1  # 索引往前移动，再次进入while循环。
        # 当不满足while条件时，就让current赋值给当前所在preIndex的索引位置，出现了-1，我们还要再加上1
        arr[preIndex + 1] = current
    return arr


"""
推到一下【3，2】


第1次循环：
preindex = -1
current = 3
arr[0] = 3

第2次循环:
preindex = 0
current = 2
进入while循环, 3 > 2：
1.把3赋值给索引1的位置上
2.preindex -1 = -1
不满足，while的条件了，跳出while循环
arr[-1 + 1] = 2 将我们最外层选择的值，赋予给前一个索引。


相当于：我们选择的值current再不断的调整位置，这个索引上原先的值不断向后移动一个位置，因为current本身就是在后面取到的值，空出来一个索引位置。
"""

if __name__ == '__main__':
    arr = insertionSort(arr=[3, 2])
    print(arr)