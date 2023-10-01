# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
for _ in range(m):
  graph.append(list(map(int, input().split())))

q = deque()

for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      q.append((i, j))

while q:
  x, y = q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= m or ny < 0 or ny >= n:
      continue

    if graph[nx][ny] == 0:
      graph[nx][ny] = graph[x][y] + 1
      q.append((nx, ny))


def solution():
  max_value = 0
  for v in graph:
    max_value = max(max(v), max_value)
    if 0 in v:
      return -1

  return max_value - 1


print(solution())
