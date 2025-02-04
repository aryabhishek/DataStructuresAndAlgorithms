"""
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

https://leetcode.com/problems/find-right-interval/
"""

from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_idx = {}
        for i, (start, end) in enumerate(intervals):
            start_idx[start] = i

        sorted_starts = sorted(list(start_idx.keys()))
        ans = []
        for start, end in intervals:
            if end in start_idx:
                ans.append(start_idx[end])
            else:
                idx = self.search(sorted_starts, end)
                if idx == len(sorted_starts):
                    ans.append(-1)
                else:
                    min_right = sorted_starts[idx]
                    ans.append(start_idx[min_right])
        return ans

    def search(self, arr, target):
        n = len(arr)
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        return low
