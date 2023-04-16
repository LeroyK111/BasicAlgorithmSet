def demo(data: list) -> list:
    result = []

    for i in data:
        if i not in result:
            result.append(i)
        else:
            result.append('_')

    return result


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 1, 6136, 3, 4, 245, 346, 23, 1, 125, 1, 3]
    data.sort(reverse=False)
    result = demo(data)
    print(result)
