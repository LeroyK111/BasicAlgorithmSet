def demo(a: int, b: int) -> int:
    c = 0
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        c = 1
    result = a // b + c
    return result


if __name__ == '__main__':
    dividend = 10
    divisor = -3
    result = demo(dividend, divisor)
    print(result)