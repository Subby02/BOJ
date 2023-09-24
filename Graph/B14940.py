# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m= map(int,input().split())

visited = [[False] * m for _ in range(n)]
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

for x in range(n):
  for y in range(m):
    if graph[x][y] == 2:
      start = (x,y)

def bfs(x,y):
  q = deque()
  q.append((x,y))
  visited[x][y] = True
  graph[x][y] = 0
  
  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      if visited[nx][ny]:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        visited[nx][ny] = True
        q.append((nx,ny))

bfs(start[0],start[1])

for x in range(n):
  for y in range(m):
    if graph[x][y] == 1 and not visited[x][y]:
      graph[x][y] = -1
      
for v in graph:
  print(*v)