# 两数之和
sums = range(10)
target = 17


def tow_sum():
    for i in sums:
        for x in sums:
            if i != x and x + i == target:
                print(i, "+", x, "=", target)


if __name__ == '__main__':
    tow_sum()
