def demo(data: list, k: int) -> list:
    count = int(len(data) / k)
    result = []
    start = 0
    for i in range(count):
        newData = data[start:start + k]
        start = start + k
        newData.reverse()
        result.extend(newData)

    result.extend(data[start:])

    return result


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    # 修改K值
    k = 3
    result = demo(head, k)
    print(result)