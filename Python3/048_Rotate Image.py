#!usr/bin/env python3
# -*- coding:utf-8 -*-
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix


if __name__ == "__main__":
    assert Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [[7, 8, 1], [6, 9, 2], [5, 4, 3]]
