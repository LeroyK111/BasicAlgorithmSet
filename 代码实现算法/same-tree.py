class Solution(object):
    def demo(self, tree1: list, tree2: list):
        if len(tree1) == len(tree2):
            tree1.sort()
            tree2.sort()
            if tree1 == tree2:
                return True

        return False


if __name__ == "__main__":
    a = [1, 2, 3, None]
    b = [3, 1, 2]
    result = Solution().demo(a, b)
    print(result)
