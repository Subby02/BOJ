# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

sys.setrecursionlimit(10000)


def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True

  while q:
    now = q.popleft()
    print(now, end=' ')

    for i in graph[now]:
      if not visited[i]:
        visited[i] = True
        q.append(i)


def dfs(start):
  visited[start] = True
  print(start, end=' ')

  for i in graph[start]:
    if not visited[i]:
      dfs(i)


n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())

  graph[x].append(y)
  graph[y].append(x)

for i in graph:
  i.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)