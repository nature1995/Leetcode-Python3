#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''
import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m -= 1
        n -= 1
        return int(math.factorial(m + n) / (math.factorial(m) * math.factorial(n)))


if __name__ == "__main__":
    assert Solution().uniquePaths(3, 7) == 28
