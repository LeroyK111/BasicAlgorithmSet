def demo(num: int) -> bool:
    if num < 0:
        return False
    strs = list(str(num))
    if len(strs) == 1:
        return True
    strs.reverse()
    res = "".join(strs)
    if int(res) == num:
        return True
    else:
        return False


if __name__ == '__main__':
    num = 10
    result = demo(num)
    print(result)
