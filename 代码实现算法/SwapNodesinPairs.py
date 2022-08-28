def demo(data: list) -> list:
    result = []
    for index, value in enumerate(data):
        if index % 2 == 0:
            if len(data) - 1 >= index + 1:
                result.extend([data[index + 1], value])
            else:
                result.append(value)

    return result


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = demo(data)
    print(result)
