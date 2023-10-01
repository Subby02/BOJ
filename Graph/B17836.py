# https://www.acmicpc.net/problem/17836

import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

gram = [-1,-1]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  sword = 1e9

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if nx == n-1 and ny == m-1:
        return min(graph[nx][ny] , sword)

      if visited[nx][ny]:
        continue

      if graph[nx][ny] == 1:
        continue

      if graph[nx][ny] == 2:
        sword = (m-1-nx) + (n-1-ny) + graph[x][y] + 1

      graph[nx][ny] = graph[x][y] + 1
      visited[nx][ny] = True
      q.append((nx,ny))

  return sword

time = bfs(0,0)

if t < time :
  print('Fail')
else:
  print(time)