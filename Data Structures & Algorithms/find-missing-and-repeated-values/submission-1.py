class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()

        double = 0
        missing = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])
        

        for num in range(1, len(grid) * len(grid) + 1):
            if num not in seen:
                missing = num
                return [double, missing]