"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description
"""


class BruteForce: # Doesn't work for large inputs
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 2:
            return -1

        ans = -1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.is_digit_sum_equal(arr[i], arr[j]):
                    ans = max(ans, arr[i] + arr[j])
                    print(ans)

        return ans

    def is_digit_sum_equal(self, n1, n2):
        n1_sum = n2_sum = 0

        while n1:
            n1_sum += n1 % 10
            n1 //= 10

        while n2:
            n2_sum += n2 % 10
            n2 //= 10

        return n1_sum == n2_sum

class Solution: # using map
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 2:
            return -1
        
        digit_map = {}
        ans = -1

        for num in arr:
            d_sum = self.digit_sum(num)
            if d_sum in digit_map:
                ans = max(ans, num + digit_map[d_sum])
            digit_map[d_sum] = max(num, digit_map.get(d_sum, 0))
        
        return ans
        
    def digit_sum(self, n):
        total = 0

        while n:
            total += n % 10
            n //= 10
        
        return total