#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
# 思路一：
# 遍历法，On:
# 算法过程：遍历数组，用onesum去维护当前元素加起来的和。当onesum出现小于0的情况时，我们把它设为0。然后每次都更新全局最大值。

# 算法证明：一开始思考数组是个空的，把我们每次选一个nums[i]加入onesum看成当前数组新增了一个元素，也就是用动态的眼光去思考。
# 过程很简单，代码很短，但为什么这样就能达到效果呢？我们进行的加和是按顺序来的，从数组第一个开始加。
# 当我们的i选出来后，加入onesum。这时有2种情况

# 1）假设我们这个onesum一直大于0，从未被<0过。那也就是说我们计算的每一次的onesum都大于0，而每一次计算的onesum都是包括开头元
# 素的一段子序列（尾部一直随i变化）。看似我们没有考虑所有可能序列，但实际上所有可能的序列都已经被考虑过了。这里简单讲一下，
# 待会po原文。
#    a)以当前子序列开头为开头，中间任一处结尾的序列。这种情况是一直在扫描的，也有一直保存更新，所以不用怕丢失信息。
#    b)以当前子序列结尾为结尾，中间任一处开头的序列。这种情况一定的和小于以当前子序列开头为开头，结尾为结尾的序列。因为前
# 面缺失的那一段经过我们的前提，它也是加和大于0的。
#    c)以中间元素为开头和结尾的序列。和小于以当前子序列开头为开头，此分序列结尾为结尾的序列。因为前面缺失的那一段经过我们
# 的前提，它也是加和大于0的。

# 2）出现小于0的情况，就说明我们当前形成的这个子序是第一次出现小于0的情况。现在至少我们要新形成的连续数组不能在整个的包括之前
# 的连续子序了，因为我们在之前的那个连续子序里加出了<0的情况。但问题是我们需不需要保留一些呢？是不是所有以当前子序结尾为结尾的
# 任意开头的子序都要被舍弃呢？答案是是的，因为那一段也一定小于0，因为那一段的加和会小于以当前子序开头为开头，当前子序结尾为结
# 尾的序列（见前面证明）。于是抛弃掉它们，重新开始新的子序。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # onesum维护当前的和
        onesum = 0
        maxsum = nums[0]
        for i in range(len(nums)):
            onesum += nums[i]
            maxsum = max(maxsum, onesum)
            # 出现onesum<0的情况，就设为0，重新累积和
            if onesum < 0:
                onesum = 0
        return maxsum


if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
