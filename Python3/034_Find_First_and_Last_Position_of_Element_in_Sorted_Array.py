#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        else:
            return [-1, 1]
        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right = j
                break
        return [left, right]





if __name__ == "__main__":
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5]
