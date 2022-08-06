"""
选择排序：双循环，选择最小（大）的一个数，记录其索引，每当运行到最外层循环时，进行位置替换。
"""


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    arr = selectionSort(arr=[123, 214, 23, 5, 512, 3, 63])
    print(arr)