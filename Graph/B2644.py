# https://www.acmicpc.net/problem/2644

import sys
from collections import deque

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = 0
  
  while q:
    now = q.popleft()

    for i in graph[now]:
      if visited[i] == -1:
        visited[i] = visited[now]+1
        q.append(i)

n = int(sys.stdin.readline())

a, b = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
  x , y = map(int,sys.stdin.readline().split())

  graph[x].append(y)
  graph[y].append(x)

bfs(a)

print(visited[b])