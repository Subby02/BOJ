# https://www.acmicpc.net/problem/1012

# stack DFS

import sys

def dfs(x,y):
  stack = []
  stack.append((x,y))

  result = False
  while stack:
    x , y = stack.pop(0)

    if x >= 0 and x < m and y >= 0 and y < n:
      if graph[x][y] == 1:
        graph[x][y] = 0

        stack.append((x-1,y))
        stack.append((x+1,y))
        stack.append((x,y-1))
        stack.append((x,y+1))

        result = True
  return result
      

t = int(sys.stdin.readline())

for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().split())

  graph = [[0] * n for _ in range(m)]
  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1

  cnt = 0
  for x in range(m):
    for y in range(n):
      if dfs(x,y):
        cnt += 1
  
  print(cnt)

# 재귀함수 DFS

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
  if x < 0 or x >= m or y < 0 or y >= n:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

    return True

  return False

t = int(sys.stdin.readline())

for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().split())

  graph = [[0] * n for _ in range(m)]
  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1

  cnt = 0
  for y in range(n):
    for x in range(m):
      if dfs(x,y):
        cnt += 1
  
  print(cnt)