"""
python中对指针进行了良好的封装，如果想实现链表，图之类的数据结构。
（C语言中提取出来的）必须自写链表类，模仿去写方法（极其不推荐啊）
"""


def addTwoNum():
    l1.reverse()
    l2.reverse()
    dt = []
    for item in [l1, l2]:
        data = map(lambda i: str(i), item)
        # 存放列表
        data = "".join(data)
        dt.append(data)

    done = int(dt[0]) + int(dt[-1])
    done = list(map(lambda i: int(i), list(str(done))))
    return done


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [3, 2, 1]
    done = addTwoNum()
    print(done)