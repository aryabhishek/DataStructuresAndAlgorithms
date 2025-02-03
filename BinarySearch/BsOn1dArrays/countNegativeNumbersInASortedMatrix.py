"""

"""


from typing import List


class BruteForce:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1

        return count

class Better:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for row in grid:
            ub = self.upperBound(row, 0)
            count += n - ub
        
        return count
    
    def upperBound(self, arr, target: str) -> str:
        n = len(arr)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            if arr[m] < target:
                r = m - 1
            else:
                l = m + 1
        return l


class Best:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        row = m - 1
        col = 0

        while row >= 0 and col < n:
            if grid[row][col] >= 0:
                col += 1
            else:
                count += n - col
                row -= 1
        return count