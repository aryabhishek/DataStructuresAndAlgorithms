"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

https://leetcode.com/problems/arranging-coins/description/
"""

from math import ceil


class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0

        l, r = 1, ceil(n / 2)

        while l <= r:
            m = l + (r - l) // 2

            if m * (m + 1) / 2 <= n:
                ans = m
                l = m + 1
            elif m * m < n:
                l = m + 1
            else:
                r = m - 1

        return ans
