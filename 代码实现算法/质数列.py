# coding=utf-8
"""
方法一,利用质数除了1和它本身，其它数都不能被整除的特性，加入标志符z进行质数的筛选。
"""


def ff_1():
    size_max = 100
    zhishu = [1]
    for i in range(2, (size_max + 1)):
        z = 0
        for x in range(2, i):
            y = i % x
            if y == 0:
                z = 1
                continue

        if z == 0:
            zhishu.append(i)
    print(zhishu)


"""
方法二,利用质数是所有非质数的因数，构造循环判断
"""


def ff_2():
    size_max = 100
    zhishu = [1]
    for i in range(2, (size_max + 1)):
        z = 0
        for x in range(2, i):
            y = i / x
            if y in zhishu:
                z = 1
                continue
        if z == 0:
            zhishu.append(i)
    print(zhishu)


"""
方法三，利用all进行筛选
"""


def ff_3():
    # 这里是利用all的特性来进行是质数筛选 all(列表中还有任何一个[0, none, "", false]) ==false
    # range(2,2) =[0]
    size_max = 100
    a = list(
        filter(lambda x: all(x % y != 0 for y in range(2, x)),
               range(2, (size_max + 1))))
    # 指定位置插入一个字符串
    a.insert(0, 1)
    print(a)


if __name__ == "__main__":
    ff_1()
    ff_2()
    ff_3()
