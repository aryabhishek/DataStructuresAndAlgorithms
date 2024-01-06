"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Link: https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans