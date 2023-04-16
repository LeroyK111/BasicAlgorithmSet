def demo(data: list, target: int):
    try:

        result = data.index(target)

    except ValueError:

        result = -1

    return result


if __name__ == '__main__':
    result = demo([2, 3, 1, 3, 124], 0)
    print(result)