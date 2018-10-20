#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, nums, result):
        if not nums:
            result.append(current + [])
            return
        else:
            for i, v in enumerate(nums):
                current.append(nums[i])
                self.get_permute(current, nums[:i] + nums[i + 1:], result)
                current.pop()


if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
