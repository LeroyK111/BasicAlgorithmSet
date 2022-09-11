class Solution:

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find the tail of the array to change
        right = len(nums) - 1
        left = right - 1
        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1

        # If the next permutation exists, then find the next highest element
        # We find this element using a Binary Search to swap with the first.


# Then swap them
        if left != -1:
            target = nums[left]
            i, j = left + 1, right
            while i <= j:
                k = (i + j) // 2
                num = nums[k]
                if num <= target:
                    j = k - 1
                else:
                    i = k + 1
            nums[left], nums[j] = nums[j], nums[left]

        # reverse the tail of the array, not including the first element.
        left += 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    demo = Solution()
    a = [2, 1, 3, 4]
    demo.nextPermutation(a)
    print(a)
