from typing import List
from collections import deque
from heapq import *
class Solution:
    def __init__(self):
        self.forest = []
        self.m = 0
        self.n = 0
    def bfs(self, x: int, y: int, k: int, l: int) -> int:
        queue = deque([(0,x,y)])
        visited = {(x,y)}
        result = -1
        while queue:
            res,x,y = queue.popleft()
            if x == k and y == l:
                result = res
                break
            if (x+1,y) not in visited and x+1 >= 0 and x+1 < self.m and y >= 0 and y < self.n and self.forest[x+1][y] >= 1:
                queue.append((res+1,x+1,y))
                visited.add((x+1,y))
            if (x,y+1) not in visited and x >= 0 and x < self.m and y+1 >= 0 and y+1 < self.n and self.forest[x][y+1] >= 1:
                queue.append((res+1,x,y+1))
                visited.add((x,y+1))
            if (x-1,y) not in visited and x-1 >= 0 and x-1 < self.m and y >= 0 and y < self.n and self.forest[x-1][y] >= 1:
                queue.append((res+1,x-1,y))
                visited.add((x-1,y))
            if (x,y-1) not in visited and x >= 0 and x < self.m and y-1 >= 0 and y-1 < self.n and self.forest[x][y-1] >= 1:
                queue.append((res+1,x,y-1))
                visited.add((x,y-1))
        return result
    def cutOffTree(self, forest: List[List[int]]) -> int:
        all = []
        self.m = len(forest)
        self.n = len(forest[0])
        for i in range(self.m):
            for j in range(self.n):
                if forest[i][j] > 1:
                    heappush(all,(forest[i][j],i,j))
        self.forest = forest
        current_x = 0
        current_y = 0
        result = 0
        while all:
            znach, x, y = heappop(all)
            new = self.bfs(current_x,current_y,x,y)
            if new == -1:
                result = -1
                break
            result += new
            current_x,current_y=x,y
        return result
s = Solution()
n = int(input('Enter n\n'))
forest = []
for i in range(n):
    forest.append(list(map(int,input('Enter n elements through the space\n').split())))
print('Result:',s.cutOffTree(forest))
