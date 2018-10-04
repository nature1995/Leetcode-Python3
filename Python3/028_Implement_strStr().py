#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question
'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        i = 0
        needleL = len(needle)
        while i < len(haystack):
            a = haystack[i:i + needleL]
            if a == needle:
                return i
            else:
                index = 0
                try:
                    index = needle.rindex(haystack[i + needleL])
                except Exception:
                    i += needleL + 1
                i += needleL - index
        return -1


if __name__ == "__main__":
    assert Solution().strStr("abcdefg", "ab") == 0
    assert Solution().strStr("abcdefg", "bc") == 1
    assert Solution().strStr("abcdefg", "cd") == 2
    assert Solution().strStr("abcdefg", "fg") == 5
    assert Solution().strStr("abcdefg", "bcf") == -1

