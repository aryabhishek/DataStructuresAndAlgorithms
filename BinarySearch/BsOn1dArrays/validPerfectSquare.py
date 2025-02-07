"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

https://leetcode.com/problems/valid-perfect-square/description/
"""

from math import ceil


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, ceil(num / 2)

        while l <= r:
            m = l + (r - l) // 2

            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                r = m - 1

        return False
