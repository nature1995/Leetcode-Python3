#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 1
        start = 0
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                nums[index] = nums[i]
                index += 1
                start = i
        return index


if __name__ == "__main__":
    assert Solution().removeDuplicates([1, 1, 2]) == 2

