from typing import List
import copy
"""
开什么玩笑
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nums = [[None] for _ in range(n + 1)]
        nums[1] = [TreeNode(1)]

        def modify_val(root, modify):
            if not root:
                return None
            temp = copy.copy(root)
            temp.val = root.val + modify
            temp.left = modify_val(root.left, modify)
            temp.right = modify_val(root.right, modify)
            return temp

        if n == 1:
            return nums[1]
        for i in range(2, n + 1):
            nums[i] = []
            for j in range(i):
                for k in nums[j]:
                    for l in nums[i - 1 - j]:
                        new = TreeNode(j + 1)
                        new.left = k
                        new.right = modify_val(l, j + 1)
                        if new:
                            nums[i].append(new)
        return nums[n]
