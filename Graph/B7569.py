# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

graph = []
for i in range(h):
  graph.append([])
  for _ in range(m):
    graph[i].append(list(map(int, input().split())))

q = deque()

for i in range(h):
  for j in range(m):
    for k in range(n):
      if graph[i][j][k] == 1:
        q.append((i, j, k))

while q:
  x, y, z = q.popleft()

  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]

    if nx < 0 or nx >= h or ny < 0 or ny >= m or nz < 0 or nz >= n :
      continue

    if graph[nx][ny][nz] == 0:
      graph[nx][ny][nz] = graph[x][y][z] + 1
      q.append((nx, ny, nz))


def solution():
  max_value = 0
  for i in range(h):
    for j in range(m):
      for k in range(n):
        if graph[i][j][k] == 0:
          return -1
        max_value = max(graph[i][j][k], max_value)

  return max_value - 1


print(solution())
