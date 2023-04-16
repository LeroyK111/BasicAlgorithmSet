#!/usr/bin/python
# -*- coding: utf-8 -*-

import math



class Solution:
    def demo(self, root: list):
        if len(root) == 1:
            return True

        # 完全对称二叉树，不用树结构判断，直接选则2**n 判断
        n = math.log2(len(root))
        if math.modf(n)[0] != 0:
            start = 1
            for i in range(1, math.ceil(n)):
                # 截同级节点

                space = 2**i
                end = start + space
                nodes = root[start:end]
                start = end

                left = nodes[0:int(len(nodes)/2)]
                right = nodes[int(len(nodes)/2):]
                right.sort()    
            
                
                if left != right:
                    return False

            return True

        return False


if __name__ == "__main__":
    root = [1, 2, 2, 3, 4, 4, 3]
    result = Solution().demo(root)
    print(result)
