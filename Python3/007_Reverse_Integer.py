#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Consider positive and negative situation
        flag = 0
        if x < 0:
            flag = -1
        if x > 0:
            flag = 1
        x *= flag
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        if result > 2 ** 32 - 1:  #2的32次方
            return 0
        else:
            return result*flag


if __name__ == "__main__":
    assert Solution().reverse(654300) == 3456
    assert Solution().reverse(-321) == -123
    assert Solution().reverse(21474836470) == 0








