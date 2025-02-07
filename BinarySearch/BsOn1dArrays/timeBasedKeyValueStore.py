"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

https://leetcode.com/problems/time-based-key-value-store/description/
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.mp[key]:
            return ""

        return self.search(self.mp[key], timestamp)

    def search(self, arr, time):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid][1] == time:
                return arr[mid][0]
            elif arr[mid][1] < time:
                low = mid + 1
            else:
                high = mid - 1
        return arr[low - 1][0] if low > 0 else ""
