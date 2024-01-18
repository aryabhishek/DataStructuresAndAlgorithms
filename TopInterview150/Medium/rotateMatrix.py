"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Link: https://leetcode.com/problems/rotate-image
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(n - 1):
            print(matrix)
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
