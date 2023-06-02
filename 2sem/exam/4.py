from typing import List, Dict
class Solution:
    def __init__(self):
        self.graph = dict()
        self.goal = 0
        self.goaltime = 0
        self.p = 0
    def dfs(self, visited: Dict, current: int, time: int, p: int):
        if current == self.goal and (current not in self.graph or time == self.goaltime or (current in self.graph and self.graph[current] <= visited)):
            if time <= self.goaltime:
                self.p = p
                return
            else:
                return
        if current in self.graph:
            queue = self.graph[current]
            l = len(queue) - len(queue.intersection(visited))
            for x in queue:
                if x not in visited:
                    visited1 = visited.copy()
                    visited1.add(x)
                    self.dfs(visited1, x, time+1, p/l)
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        for i in range(len(edges)):
            x,y = edges[i]
            if x not in self.graph:
                self.graph[x] = set([y])
            else:
                new = self.graph[x]
                new.add(y)
                self.graph[x] = new
            if y not in self.graph:
                self.graph[y] = set([x])
            else:
                new = self.graph[y]
                new.add(x)
                self.graph[y] = new
        self.goal = target
        self.goaltime = t
        visited = set([1])
        self.dfs(visited, 1, 0, 1)
        return self.p
s = Solution()
n = int(input('Enter n\n'))
edges = []
ne = int(input('Enter amount of edges\n'))
for i in range(ne):
    edges.append(list(map(int,input('Enter edge (pair of int through space)\n').split())))
t = int(input('Enter t\n'))
target = int(input('Enter target\n'))
print('Result:',s.frogPosition(n,edges,t,target))
