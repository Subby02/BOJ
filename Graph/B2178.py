# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
  array = list(input().rstrip())
  graph.append(list(map(int, array)))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
  q = deque()
  q.append((x,y))

  while q:
    now = q.popleft()
    
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
  
      if 0 > nx or nx >= n or 0 > ny or ny >= m:
        continue
  
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[now[0]][now[1]] + 1
        q.append((nx,ny))


bfs(0, 0)

print(graph[-1][-1])
