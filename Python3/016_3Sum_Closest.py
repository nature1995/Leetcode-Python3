#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        # Init the distance between result and target with a very large number
        distance = pow(2, 32) - 1
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                li = nums[i] + nums[left] + nums[right]
                if li == target:
                    return target
                if abs(li - target) < distance:
                    result = li
                    distance = abs(li - target)
                elif li > target:
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == "__main__":
    assert Solution().threeSumClosest([1, 1, 1, 1], -100) == 3
