"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

https://leetcode.cohttphttps://leetcode.com/problems/snapshot-array/description/s://leetcode.com/problems/snapshot-array/description/m/problems/snapshot-array/description/
"""

from collections import defaultdict


class SnapshotArray:

    def __init__(self, length: int):
        self.store = defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.store[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.store[index]
        if not arr or snap_id < arr[0][0]:
            return 0

        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid - 1

        return arr[high][1]
