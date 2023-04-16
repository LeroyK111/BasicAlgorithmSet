#!/usr/bin/python
# -*- coding: utf-8 -*-
from TreeNode import Node


class Solution:
    def errorRecovery(self, root: Node):
        result = root.PreorderTraversal(root)

        return result


if __name__ == "__main__":
    data = [1, 3, None, None, 2]
    root = Node(data[0])
    for i in data[1:]:
        root.insert(i)

    result = Solution().errorRecovery(root)
    print(result)
