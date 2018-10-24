#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
# 思路二：
# 动态规划 On

# 算法过程：
# 设sum[i]为以第i个元素结尾的最大的连续子数组的和。假设对于元素i，所有以它前面的元素结尾的子数组的长度都已经求得，那么以
# 第i个元素结尾且和最大的连续子数组实际上，要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素，
# 即sum[i]
# = max(sum[i-1] + a[i], a[i])。可以通过判断sum[i-1] + a[i]是否大于a[i]来做选择，而这实际上等价于判断sum[i-1]是否大于0。
# 由于每次运算只需要前一次的结果，因此并不需要像普通的动态规划那样保留之前所有的计算结果，只需要保留上一次的即可，因此算法
# 的时间和空间复杂度都很小

# 算法证明：这道题的代码我直接使用了题目数据中的nums数组，因为只要遍历一遍。nums[i]表示的是以当前这第i号元素结尾（看清了一定
# 要包含当前的这个i）的话，最大的值无非就是看以i-1结尾的最大和的子序能不能加上我这个nums[i]，如果nums[i]>0的话，则加上。注意
# 我代码中没有显式地去这样判断，不过我的Max表达的就是这个意思，然后我们把nums[i]确定下来。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            subMaxSum = max(nums[i] + nums[i - 1], nums[i])
            nums[i] = subMaxSum  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
        return max(nums)


if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

