from typing import List
import sys
class Solution:
    def __init__(self):
        self.grid = []
        self.results = []
    def find(self, i: int, j: int, k: int, l: int) -> int:
        if i >= len(self.grid) or j >= len(self.grid) or k >= len(self.grid) or l >= len(self.grid) or self.grid[i][j] == -1 or self.grid[k][l] == -1:
            return -sys.maxsize - 1
        if self.results[i][j][k] != -1:
            return self.results[i][j][k]
        res = self.grid[i][j]
        if i == len(self.grid) -1 and j == len(self.grid)-1 and k == len(self.grid) -1 and l == len(self.grid)-1:
            return res
        if i != k or j != l:
            res += self.grid[k][l]
        res += max(self.find(i+1,j,k+1,l),self.find(i,j+1,k,l+1),self.find(i+1,j,k,l+1),self.find(i,j+1,k+1,l))
        self.results[i][j][k] = res
        return self.results[i][j][k]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.results = [[[-1 for i in range(len(grid))] for j in range(len(grid))] for k in range(len(grid))]
        return max(self.find(0,0,0,0),0)
s = Solution()
n = int(input('Enter n\n'))
grid = []
for i in range(n):
    grid.append(list(map(int,input('Enter element through spaces\n').split())))
print('Result:',s.cherryPickup(grid))
