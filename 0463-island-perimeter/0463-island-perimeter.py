class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        surr = 0
        R = len(grid)
        C = len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    if i - 1 < 0:
                        surr += 1
                    elif grid[i-1][j] == 0:
                        surr += 1
                    if i + 1 > R - 1:
                        surr += 1
                    elif grid[i+1][j] == 0:
                        surr += 1
                    if j - 1 < 0:
                        surr += 1
                    elif grid[i][j-1] == 0:
                        surr += 1
                    if j + 1 > C - 1:
                        surr += 1
                    elif grid[i][j+1] == 0:
                        surr += 1
        return surr
                        


        