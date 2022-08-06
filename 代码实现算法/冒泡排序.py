"""
双循环，进行两两间对比，始终把大数后移.
"""


def bubbleSort(arr):
    for i in range(1, len(arr) - 1):
        # 外层负责对索引的缩减
        for j in range(len(arr) - i):
            # 内层负责循环判断，并替换数据
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = bubbleSort(arr=[23, 124, 2, 5, 12])
    print(arr)
