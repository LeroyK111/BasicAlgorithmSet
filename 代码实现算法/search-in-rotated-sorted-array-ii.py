class Solution:
    def demo(self, nums: list, target: int) -> bool:
        try:
            nums.index(target)
        except ValueError:
            return False
        else:
            return True


if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    result = Solution().demo(nums, target)
    print(result)
