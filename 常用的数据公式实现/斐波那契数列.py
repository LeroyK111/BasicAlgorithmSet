"""
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
"""

# 前多少项斐波那契数列


import sys


def fib_count(n) -> list:
    if n == 0:
        raise KeyError("哪有0")
    elif n == 1:
        return list(range(1))
    elif n == 2:
        return list(range(2))
    else:
        a = 0
        b = 1
        count = 3
        fib_list = list(range(2))
        while True:
            c = a + b
            a, b = b, c
            fib_list.append(c)
            if count == n:
                return fib_list
            count += 1


# 前三十个斐波那契数列，求和
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # number = fib(30)
    # print(number)
    try:
        fib_list = fib_count(int(sys.argv[1:2][0]))
    except Exception as f:
        print(f)
    else:
        print(fib_list)
