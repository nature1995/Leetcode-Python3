#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Valid str must be even
        if len(s) % 2 == 1:
            return False
        stack = []
        left = ("(", "[", "{")
        right = (")", "]", "}")
        zip(left, right)
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if left.index(p) != right.index(c):
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    assert Solution().isValid("({}){}") == True
    assert Solution().isValid("({)}") == False
    assert Solution().isValid("}}}") == False
    assert Solution().isValid("(((") == False







