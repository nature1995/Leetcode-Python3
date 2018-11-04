#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 1.0
        while abs(result ** 2 -  x) > 0.1:
            result = (result + x / result) / 2
        return int(result)


if __name__ == "__main__":
    assert Solution().mySqrt(5) == 2
    assert Solution().mySqrt(0) == 0
