#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, "", result)
        return result

    def generate(self, left, right, string, result):
        if left == 0 and right == 0:
            result.append(string)
            return
        if left > 0:
            self.generate(left - 1, right, string + "(", result)
        if right > left:
            self.generate(left, right - 1, string + ")", result)


if __name__ == "__main__":
    assert (Solution().generateParenthesis(3)) == ['((()))', '(()())', '(())()', '()(())', '()()()']

