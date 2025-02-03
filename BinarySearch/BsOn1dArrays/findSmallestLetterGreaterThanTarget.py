"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=study-plan-v2&envId=binary-search
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n - 1
        ans = None

        while l <= r:
            m = l + (r - l) // 2

            if letters[m] > target:
                ans = letters[m]
                r = m - 1
            else:
                l = m + 1
        return ans if ans else letters[0]