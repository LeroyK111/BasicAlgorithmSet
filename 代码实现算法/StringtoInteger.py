def demo(strs: str) -> int:
    strs = strs.replace(" ", "")
    result = int(strs)
    return result


if __name__ == '__main__':
    strs = " -1 0 2 8 "
    result = demo(strs)
    print(result)