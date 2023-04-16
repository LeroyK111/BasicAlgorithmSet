"""
生成二叉树
"""


class Node(object):
    def __init__(self, data):
        self.left = None  # 左节点
        self.right = None  # 右节点
        self.data = data  # 值

    def insert(self, data):
        if data is None:
            # 让-999替代none
            data = -999

        # 将新值与父节点进行比较
        if self.data:  # 非空
            if data <= self.data:  # !新值较小，放左边，考虑到none值的存在，所以小于等于，不然直接小于就行
                if self.left is None:  # 若空，则新建插入节点
                    # !新建一个对象，传入当前根节点的左节点对象，
                    self.left = Node(data)
                else:  # !否则，递归调用对象的方法，往下查找，
                    self.left.insert(data)
            elif data > self.data:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入对象
                    self.right = Node(data)
                else:  # 否则，递归往下查找
                    self.right.insert(data)
        else:
            # 空值则只有起始对象
            self.data = data

    def PrintTree(self):
        # 这里使用的还是中序遍历
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def fil(self, data: list):
        return list(map(lambda x: None if x == -999 else x, data))

    # 中序遍历
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            # 先查找左节点
            res = self.inorderTraversal(root.left)
            # 加入根节点
            res.append(root.data)
            # 开始查找右节点
            res = res + self.inorderTraversal(root.right)
        return self.fil(res)

    # 先序遍历
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return self.fil(res)

    # 后序遍历
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return self.fil(res)


if __name__ == "__main__":
    # 创建节点
    root = Node(12)
    # 插入节点
    root.insert(6)
    root.insert(14)
    root.insert(3)

    # 打印所有的树
    # root.PrintTree()

    # 中序遍历 [3, 6, 12, 14]
    result = root.inorderTraversal(root)
    print(result)
    # 先序遍历 [12, 6, 3, 14]
    result = root.PreorderTraversal(root)
    print(result)
    # 后续遍历 [3, 6, 14, 12]
    result = root.PostorderTraversal(root)
    print(result)
