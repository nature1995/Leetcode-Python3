#!usr/bin/env python
# -*- coding:utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)
        locations = [-1 for i in range(256)]
        print(locations)
        index = -1
        m = 0
        for i, v in enumerate(s):
            #如果出现的字符就需要更新index为当前字符的位置
            if (locations[ord(v)] > index):
                index = locations[ord(v)]
            m = max(m, i - index)
            #确定字符的位置，相同字符的位置一样
            locations[ord(v)] = i
        return m


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("bccab"))


