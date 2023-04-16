#!/usr/bin/python
# -*- coding: utf-8 -*-


class solution:
    def run(self, nums: list)->list:
        nums.sort()
        return nums
        
        
        
        





if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    D = solution().run(nums)
    print(D)

    