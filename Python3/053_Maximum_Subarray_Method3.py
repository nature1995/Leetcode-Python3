#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
# 思路三：
#
# 分治递归
# 算法过程：
# 分治法，最大子序和要么在左半部分，要么在右半部分，要么就横跨两部分（即包括左半部分的最后一个元素，和右半部分的第一个元素）
# 。返回这三种情况的最大值即可。第三种情况，其中包括左半部分最后一个元素的情形，需要挨个往前遍历，更新最大值。包含右半部分的
# 第一个元素的情况类似。总的时间复杂度O(nlogn)

# 算法证明：
# 总的来说还是超级巧妙的。不断的切不断的切数组，把一块数组看成左中右三个部分。实际上这有点像枚举，但我们在枚举时利用了二分
# 的思路，优化了很多。所以枚举当然可以达到我们的目标了，因为我们不断在计算以一定包括中间节点的子序的最大和。


class Solution(object):
    def maxSubArray(self, nums):
        # 主函数
        left = 0
        # 左右边界
        right = len(nums) - 1
        # 求最大和
        maxSum = self.divide(nums, left, right)
        return maxSum

    def divide(self, nums, left, right):
        # 如果只有一个元素就返回
        if left == right:
            return nums[left]
        # 确立中心点
        center = (left + right) // 2
        # 求子序在中心点左边的和
        leftMaxSum = self.divide(nums, left, center)
        # 求子序在中心点右边的和
        rightMaxSum = self.divide(nums, center + 1, right)

        # 求子序横跨2边的和，分成左边界和和右边界和
        leftBorderSum = nums[center]
        leftSum = nums[center]
        for i in range(center - 1, left - 1, -1):
            leftSum += nums[i]
            if leftSum > leftBorderSum:
                # 不断更新左区块的最大值
                leftBorderSum = leftSum

        rightBorderSum = nums[center + 1]
        rightSum = nums[center + 1]
        for i in range(center + 2, right + 1):
            rightSum += nums[i]
            if rightSum > rightBorderSum:
                # 不断更新右区块的最大值
                rightBorderSum = rightSum
        # 左边界的和 + 右边那块的和
        BorderSum = leftBorderSum + rightBorderSum
        return max(leftMaxSum, rightMaxSum, BorderSum)


if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

