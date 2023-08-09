# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
  array = list(input().rstrip())
  graph.append(list(map(int, array)))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
  cnt = 1
  graph[x][y] = 0
  q = deque()
  q.append((x, y))

  while q:
    now = q.popleft()

    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]

      if 0 > nx or nx >= n or 0 > ny or ny >= n:
        continue

      if graph[nx][ny] == 1:
        cnt += 1
        graph[nx][ny] = 0
        q.append((nx, ny))

  return cnt


result = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      result.append(bfs(i, j))
result.sort()

print(len(result))
for v in result:
  print(v)
