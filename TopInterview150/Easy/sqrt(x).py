"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.\=
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Link: https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150
"""

from math import ceil


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, ceil(x / 2)

        while l <= r:
            m = l + (r - l) // 2

            if m * m <= x < (m + 1) * (m + 1):
                return m
            if m * m < x:
                l = m + 1
            elif m * m > x:
                r = m - 1
