#!/usr/bin/python
# -*- coding: utf-8 -*-


def demo(nums: list[int]) -> bool:
    index = 0
    first_value = nums[index]
    if first_value <= 0:
        return False

    while True:
        index = first_value + index
        try:
            first_value = nums[index]
        except IndexError as identifier:
            if first_value == nums[-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # true
    result = demo(nums)
    print(result)